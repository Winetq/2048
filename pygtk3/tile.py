import configparser

import gi

from converter import convert_hex_to_rgb

gi.require_version("Gtk", "3.0")

# read configuration
cfg = configparser.ConfigParser()
cfg.read('settings.ini')


class Tile:

    def __init__(self, matrix, value):
        super(Tile, self).__init__()
        self.matrix = matrix
        self.value = value
        self.x = 0
        self.y = 0
        self.width = self.matrix.tile_size
        self.height = self.matrix.tile_size
        self.cell_color = cfg.get("Appearance", "color.%s" % value if value <= 2048 else 2048)
        if value > 4:
            self.text_color = cfg.get("Appearance", "color.text.light")
        else:
            self.text_color = cfg.get("Appearance", "color.text.dark")

    def set_value(self, value):
        self.value = value
        self.cell_color = cfg.get("Appearance", "color.%s" % value if value <= 2048 else 2048)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self, cr):
        rgb = convert_hex_to_rgb(self.cell_color)
        cr.set_source_rgb(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
        cr.rectangle(self.x, self.y, self.width, self.height)
        cr.fill()
        rgb = convert_hex_to_rgb(self.text_color)
        cr.set_source_rgb(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
        if self.value < 10:
            cr.set_font_size(28)
            cr.move_to(self.x + self.width * 0.375, self.y + self.height * 0.675)
        elif self.value < 100:
            cr.set_font_size(27)
            cr.move_to(self.x + self.width * 0.25, self.y + self.height * 0.675)
        elif self.value < 1000:
            cr.set_font_size(26)
            cr.move_to(self.x + self.width * 0.125, self.y + self.height * 0.675)
        else:
            cr.set_font_size(25)
            cr.move_to(self.x + self.width * 0, self.y + self.height * 0.675)
        cr.show_text(str(self.value))
