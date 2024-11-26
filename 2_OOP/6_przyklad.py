class Zasob:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.__wypozyczony = False

    def wypozycz(self):
        if not self.__wypozyczony:
            self.__wypozyczony = True
            return f'Zasob {self.tytul} zosta wypozyczony'
        else:
            return f'Zasob {self.tytul} jest już wypozyczony'

    def zwroc(self):


    def stan_wypozyczenia(self):


    def opis(self):
        return f'{self.tytul}, autor: {self.autor}, rok wydania: {self.rok_wydania}'


class Ksiazka(Zasob):        # liczba stron


class Czasopismo(Zasob)        # numer wydania
