class Pracownik:
    def __init__(self, imie, pensja_podstawowa):
        self.imie = imie
        self.pensja_podstawowa = pensja_podstawowa
        self._bonus_procent = 0

    @property
    def pensja_podstawowa(self):
        pass

    @pensja_podstawowa.getter
    def pensja_podstawowa(self):
        print(f'Zapytanie o pensje pracownika {self.imie}')
        return self._pensja_podstawowa

    @pensja_podstawowa.setter
    def pensja_podstawowa(self, value):
        if value < 0:
            raise ValueError('Pensja nie moze byc mniejsz aod 0')
        print(f'Pensja pracownika {self.imie} zmieniona z {self._pensja_podstawowa} na {value}')
        self._pensja_podstawowa = value

    @property
    def bonus_procent(self):
        return self._bonus_procent

    @bonus_procent.setter
    def bonus_procent(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Nie ma takiego bonusu')
        self._bonus_procent = value

    def oblicz_wynagrodzenie(self):
        return self._pensja_podstawowa * (1 + self._bonus_procent / 100)

    def __str__(self):
        return (f'{self.imie}: pensja podstawowa = {self._pensja_podstawowa}, '
                f'bonus = {self.bonus_procent}%, '
                f'wynagordzenie calkowite = {self.oblicz_wynagrodzenie()}')

pracownik = Pracownik("Jan Kowalski", 3000)
print(pracownik)

pracownik.pensja_podstawowa = 3500
pracownik.bonus_procent = 15
print(pracownik)

try:
    pracownik.bonus_procent = 110
except ValueError as e:
    print(e)