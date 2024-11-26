class Osoba:
    def __init__(self, imie, wiek):
        self._imie = imie
        self._wiek = wiek

    def get_imie(self):
        return self._imie

    def set_imie(self, imie):
        if not imie:
            raise ValueError("Imie nie może być puste")
        self._imie = imie

    def getwiek(self):
        return self._wiek

    def setwiek(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Wiek musi byc dodatnią liczbą całkowitą")
        self._wiek = value

osoba = Osoba('Kamil', 36)
print(osoba.get_imie())
print(osoba.getwiek())
osoba.set_imie('Ela')
osoba.setwiek(25)
print(osoba.get_imie())
print(osoba.getwiek())



