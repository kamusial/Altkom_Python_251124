class Osoba:
    def __init__(self, imie, wiek):
        self._imie = imie
        self._wiek = wiek

    @property
    def imie(self):
        pass

    @imie.getter
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, imie):
        if not imie:
            raise ValueError("Imie nie może być puste")
        self._imie = imie


    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Wiek musi byc dodatnią liczbą całkowitą")
        self._wiek = value

osoba = Osoba('Kamil', 36)
print(osoba.imie)
print(osoba.wiek)
osoba.imie = 'Ela'
osoba.wiek = 25
print(osoba.imie)
print(osoba.wiek)

try:
    osoba.wiek = -25
except ValueError as e:
    print(e)


