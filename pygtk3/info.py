import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Info(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Informacje o grze", parent)
        Gtk.Dialog.set_resizable(self, False)
        self.set_default_size(300, 300)

        label = Gtk.Label(
            " W grze 2048 mamy planszę kwadratowych klocków o wymiarach 4x4. Do sterowania \n wykorzystujemy"
            " strzałki klawiatury. Rozgrywkę zaczynamy z jednym klockiem z cyfrą \n 2 lub 4. Gra 2048"
            " polega na przesuwaniu kwadratowych pól, których wartości sumują \n się w chwili ich połączenia."
            " Zastrzeżenie jest takie, że dodawać do siebie można \n jedynie klocki o tej samej wartości. Celem gry jest"
            " uzyskanie wyniku 2048. \n Gracz może przemieszczać kwadratowe klocki w pionie i w poziomie, każdy ruch \n"
            " przesuwa je o jedno pole w wybranym kierunku, a po jego wykonaniu na planszy \n odkryte zostaje jedno pole z"
            " cyfrą 2 lub 4. Klocki zatrzymują się, gdy natrafią na \n koniec planszy lub klocek o innej wartości. Gracz"
            " wygrywa, gdy osiągnie wynik \n 2048, a przegrywa, gdy wszystkie pola będą zajęte."
        )

        label.set_size_request(300, 300)

        box = self.get_content_area()
        box.add(label)
        self.show_all()
