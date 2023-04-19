# import standard libraries
import configparser

# import third-party libraries
from PyQt5 import QtGui, QtCore

# read configuration
cfg = configparser.ConfigParser()
cfg.read('settings.ini')


class Tile(QtCore.QObject):

    def __init__(self, matrix, value):
        super(Tile, self).__init__()
        self.matrix = matrix
        self.value = value
        self.x = 0
        self.y = 0
        self.width = self.matrix.tile_size
        self.height = self.matrix.tile_size
        self.cell_color = QtGui.QColor("#" + cfg.get("Appearance", "color.%s" % value if value <= 2048 else 2048))
        if value > 4:
            self.text_color = QtGui.QColor("#" + cfg.get("Appearance", "color.text.light"))
        else:
            self.text_color = QtGui.QColor("#" + cfg.get("Appearance", "color.text.dark"))
        self.font = QtGui.QFont()

    def set_value(self, value):
        self.value = value
        self.cell_color = QtGui.QColor("#" + cfg.get("Appearance", "color.%s" % value if value <= 2048 else 2048))

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self, painter):
        painter.setPen(self.cell_color)
        painter.setBrush(self.cell_color)
        painter.drawRoundedRect(QtCore.QRect(self.x, self.y, self.width, self.height),
                                3, 3,
                                QtCore.Qt.AbsoluteSize)
        painter.setPen(self.text_color)
        self.font.setPixelSize(25)
        painter.setFont(self.font)
        painter.drawText(QtCore.QRect(self.x, self.y, self.width, self.height),
                         QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                         str(self.value))
