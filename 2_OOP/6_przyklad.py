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
        if self.__wypozyczony:
            self.__wypozyczy = False
            return f'Zasob {self.tytul} został zwrocony'
        else:
            return f'Zasób {self.tytul} nie był wypozyczony'

    def stan_wypozyczenia(self):
        return self.__wypozyczony

    def opis(self):
        return f'{self.tytul}, autor: {self.autor}, rok wydania: {self.rok_wydania}'


class Ksiazka(Zasob):        # liczba stron
    def __init__(self, tytul, autor, rok_wydania, liczba_stron):
        super().__init__(tytul, autor, rok_wydania)
        self.liczba_stron = liczba_stron

    def opis(self):
        return f'{super().opis()}, liczba stron: {self.liczba_stron}'

class Czasopismo(Zasob):        # numer wydania
    def __init__(self, tytul, autor, rok_wydania, numer_wydania):
        super().__init__(tytul, autor, rok_wydania)
        self.numer_wydania = numer_wydania

    def opis(self):
        return f'{super().opis()}, numer wydania: {self.numer_wydania}'

class Biblioteka:
    def __init__(self):
        self.zasoby = []

    def dodaj_zasob(self, zasob):
        self.zasoby.append(zasob)

    def wypozycz_zasob(self, tytul):
        for zasob in self.zasoby:
            if zasob.tytul == tytul:
                return zasob.wypozycz()

    def zwroc_zasob(self, tytul):
        for zasob in self.zasoby:
            if zasob.tytul == tytul:
                return zasob.zwroc()

    def wyswietl_zasoby(self):
        return [zasob.opis() for zasob in self.zasoby]

ksiazka1 = Ksiazka('Pinokio', 'Anders', 1987, 322)
czasopismo1 = Czasopismo('Kaczor Donald', 'Donald', 2022, 4)

biblioteka = Biblioteka()
biblioteka.dodaj_zasob(ksiazka1)
biblioteka.dodaj_zasob(czasopismo1)
print(biblioteka.wyswietl_zasoby())

print(biblioteka.wypozycz_zasob('Pinokio'))
print(biblioteka.wypozycz_zasob('W pustyni i w puszczy'))

