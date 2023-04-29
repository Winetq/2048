# import standard libraries
import configparser
import sys

# import third-party libraries
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QAction

from canvas import Canvas
from matrix import Matrix
from pyqt5.info import Info

# read configuration
cfg = configparser.ConfigParser()
cfg.read('settings.ini')


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setFixedSize(int(cfg.get("Window", "width")), int(cfg.get("Window", "height")))
        self.setWindowTitle(cfg.get("Locale", "title"))
        self.setAutoFillBackground(True)

        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), QtGui.QColor("#" + cfg.get("Appearance", "color.background")))
        self.setPalette(pallete)

        self.state = "playing"

        self.matrix = Matrix(self)
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

        self.createMenu()

        self.show()

    def createMenu(self):
        infoAction = QAction('&O grze', self)
        infoAction.triggered.connect(self.clicked)

        otherAction = QAction('&Nowa gra', self)
        otherAction.triggered.connect(self.start_new_game)

        menu = self.menuBar()

        infoMenu = menu.addMenu('&Informacje')
        infoMenu.addAction(infoAction)

        otherMenu = menu.addMenu('&Inne')
        otherMenu.addAction(otherAction)

    def clicked(self):
        info = Info()
        info.exec_()

    def start_new_game(self):
        self.close()
        self.__init__()

    def keyPressEvent(self, event):
        if self.state == "lose" or self.state == "win":
            return
        if not event.isAutoRepeat():
            self.matrix.modified = False
            if event.key() == QtCore.Qt.Key_Left:
                self.matrix.left()
            elif event.key() == QtCore.Qt.Key_Up:
                self.matrix.up()
            elif event.key() == QtCore.Qt.Key_Right:
                self.matrix.right()
            elif event.key() == QtCore.Qt.Key_Down:
                self.matrix.down()
            if self.matrix.modified:
                self.matrix.spawn()
                self.check_state()
                self.update()

    def check_state(self):
        if self.matrix.check_state() is False:
            self.state = "lose"
        elif self.matrix.find_2048():
            self.state = "win"
        else:
            self.state = "playing"

    def resizeEvent(self, event):
        size = event.size()
        width = size.width()
        height = size.height()
        self.canvas.resize(width, height)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = Main()
    sys.exit(app.exec_())
