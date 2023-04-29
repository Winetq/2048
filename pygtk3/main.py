import configparser

import gi

from converter import convert_hex_to_rgb
from info import Info
from matrix import Matrix

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# read configuration
cfg = configparser.ConfigParser()
cfg.read('settings.ini')


class Main(Gtk.Window):

    def __init__(self):
        super().__init__(title="2048")
        Gtk.Window.set_resizable(self, False)
        Gtk.Window.set_default_size(self, int(cfg.get("Window", "width")), int(cfg.get("Window", "height")))
        self.state = "playing"
        self.matrix = Matrix(self)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.createMenu()

        self.canvas = Gtk.DrawingArea()
        self.canvas.connect("draw", self.expose)
        self.box.pack_start(self.canvas, True, True, 0)

        self.add(self.box)

        self.connect("key_press_event", self.key_events)

    def expose(self, widget, cr):
        cr.set_font_size(26)
        if self.state == "win":
            cr.move_to(50 + 30, 70)
            cr.show_text(cfg.get("Locale", "win"))
        elif self.state == "lose":
            cr.move_to(50 + 85, 70)
            cr.show_text(cfg.get("Locale", "lose"))

        rgb = convert_hex_to_rgb(cfg.get("Appearance", "color.grid"))
        cr.set_source_rgb(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
        cr.rectangle(50, 100, 300, 300)
        cr.fill()

        rgb = convert_hex_to_rgb(cfg.get("Appearance", "color.cell"))
        cr.set_source_rgb(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
        for y in range(self.matrix.grid):
            for x in range(self.matrix.grid):
                self.matrix.data[y][x][0].set_x(75 + (x + 1) * self.matrix.space_between_tiles + x * self.matrix.tile_size)
                self.matrix.data[y][x][0].set_y(125 + (y + 1) * self.matrix.space_between_tiles + y * self.matrix.tile_size)
                cr.rectangle(self.matrix.data[y][x][0].x, self.matrix.data[y][x][0].y, self.matrix.tile_size, self.matrix.tile_size)
                cr.fill()

        for tile in self.matrix.cells_to_draw():
            tile.draw(cr)

    def createMenu(self):
        mb = Gtk.MenuBar()
        menu1 = Gtk.Menu()
        menu2 = Gtk.Menu()

        infoMenu = Gtk.MenuItem("Informacje")
        infoMenu.set_submenu(menu1)

        otherMenu = Gtk.MenuItem("Inne")
        otherMenu.set_submenu(menu2)

        infoAction = Gtk.MenuItem("O grze")
        infoAction.connect("activate", self.clicked)
        menu1.append(infoAction)

        otherAction = Gtk.MenuItem("Nowa gra")
        otherAction.connect("activate", self.start_new_game)
        menu2.append(otherAction)

        mb.append(infoMenu)
        mb.append(otherMenu)

        self.box.pack_start(mb, False, False, 0)

    def clicked(self, widget):
        info = Info(self)
        info.run()
        info.destroy()

    def start_new_game(self, widget):
        self.state = "playing"
        self.matrix = Matrix(self)
        self.canvas.queue_draw()

    def key_events(self, widget, event):
        if self.state == "lose" or self.state == "win":
            return

        self.matrix.modified = False

        if event.keyval == 65361:
            self.matrix.left()
        elif event.keyval == 65362:
            self.matrix.up()
        elif event.keyval == 65363:
            self.matrix.right()
        elif event.keyval == 65364:
            self.matrix.down()

        if self.matrix.modified:
            self.matrix.spawn()
            self.check_state()
            self.canvas.queue_draw()

    def check_state(self):
        if self.matrix.check_state() is False:
            self.state = "lose"
        elif self.matrix.find_2048():
            self.state = "win"
        else:
            self.state = "playing"


if __name__ == "__main__":
    win = Main()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
