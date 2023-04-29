from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class Info(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informacje o grze")
        self.setFixedSize(800, 300)

        label = QLabel(
            " W grze 2048 mamy planszę kwadratowych klocków o wymiarach 4x4. Do sterowania \n wykorzystujemy"
            " strzałki klawiatury. Rozgrywkę zaczynamy z jednym klockiem z cyfrą \n 2 lub 4. Gra 2048"
            " polega na przesuwaniu kwadratowych pól, których wartości sumują \n się w chwili ich połączenia."
            " Zastrzeżenie jest takie, że dodawać do siebie można \n jedynie klocki o tej samej wartości. Celem gry jest"
            " uzyskanie wyniku 2048. \n Gracz może przemieszczać kwadratowe klocki w pionie i w poziomie, każdy ruch \n"
            " przesuwa je o jedno pole w wybranym kierunku, a po jego wykonaniu na planszy \n odkryte zostaje jedno pole z"
            " cyfrą 2 lub 4. Klocki zatrzymują się, gdy natrafią na \n koniec planszy lub klocek o innej wartości. Gracz"
            " wygrywa, gdy osiągnie wynik \n 2048, a przegrywa, gdy wszystkie pola będą zajęte."
        )

        label.setStyleSheet("font-size: 20px;")

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
