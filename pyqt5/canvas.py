# import standard libraries
import configparser

# import third-party libraries
from PyQt5 import QtWidgets, QtGui, QtCore

# read configuration
cfg = configparser.ConfigParser()
cfg.read('settings.ini')


class Canvas(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Canvas, self).__init__(parent)
        self.parent = parent
        self.matrix = parent.matrix
        self.painter = QtGui.QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)

        font = QtGui.QFont()
        font.setPixelSize(24)
        self.painter.setFont(font)

        text_line_rect = QtCore.QRect(50, 40, 300, 50)
        if self.parent.state == "win":
            self.painter.drawText(text_line_rect, QtCore.Qt.AlignHCenter, cfg.get("Locale", "win"))
        elif self.parent.state == "lose":
            self.painter.drawText(text_line_rect, QtCore.Qt.AlignHCenter, cfg.get("Locale", "lose"))

        self.painter.setPen(QtGui.QColor("#" + cfg.get("Appearance", "color.grid")))
        self.painter.setBrush(QtGui.QColor("#" + cfg.get("Appearance", "color.grid")))
        grid = QtCore.QRect(50, 100, 300, 300)
        self.painter.drawRect(grid)

        self.painter.setPen(QtGui.QColor("#" + cfg.get("Appearance", "color.cell")))
        self.painter.setBrush(QtGui.QColor("#" + cfg.get("Appearance", "color.cell")))
        for y in range(self.matrix.grid):
            for x in range(self.matrix.grid):
                self.matrix.data[y][x][0].set_x(75 + (x + 1) * self.matrix.space_between_tiles + x * self.matrix.tile_size)
                self.matrix.data[y][x][0].set_y(125 + (y + 1) * self.matrix.space_between_tiles + y * self.matrix.tile_size)
                self.painter.drawRoundedRect(self.matrix.data[y][x][0].x,
                                             self.matrix.data[y][x][0].y,
                                             self.matrix.tile_size,
                                             self.matrix.tile_size,
                                             3, 3,
                                             QtCore.Qt.AbsoluteSize)

        for tile in self.matrix.cells_to_draw():
            tile.draw(self.painter)

        self.painter.end()
