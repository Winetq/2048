from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class Info(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informacje o grze")
        self.setGeometry(400, 400, 400, 400)

        label = QLabel(
            " W grze 2048 mamy do czynienia z planszą kwadratowych klocków o wymiarach 4x4. Do sterowania \n wykorzystujemy"
            " strzałki klawiatury. Rozgrywkę zaczynamy z jednym klockiem z cyfrą 2 lub 4. \n Krótko mówiąc, gra 2048"
            " polega na przesuwaniu kwadratowych pól, których wartości sumują się \n w chwili połączenia klocków."
            " Zastrzeżenie jest takie, że dodawać do siebie można jedynie klocki \n o tej samej wartości. Celem gry jest"
            " uzyskanie wyniku 2048. \n Gracz może przemieszczać kwadratowe klocki w pionie i w poziomie, każdy ruch \n"
            " przesuwa je o jedno pole w wybranym kierunku, a po jego wykonaniu na planszy odkryte zostaje \n jedno pole z"
            " cyfrą 2 lub 4. Klocki zatrzymują się, gdy natrafią na koniec planszy lub klocek o innej wartości. \n Gracz"
            " wygrywa, gdy osiągnie wynik 2048, a przegrywa, gdy wszystkie pola będą zajęte."
        )

        label.setStyleSheet("font-size: 20px; background-color: #fff; color: #000;")

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
