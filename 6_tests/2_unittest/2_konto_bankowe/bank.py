class KontoBankowe:
    def __init__(self, wlasciciel, saldo=0):
        self.wlasciciel = wlasciciel.title()
        self.saldo = saldo

    def wplata(self, kwota):
        if kwota <= 0:
            raise ValueError('Kwota musi być większa od zera')
        self.saldo += kwota

    def wyplata(self, kwota):
        if kwota > self.saldo:
            raise ValueError('Niewystarczające środki')
        if kwota <= 0:
            raise ValueError('Kwota musi być większa niż zero')
        self.saldo -= kwota

    def sprawdz_saldo(self):
        return self.saldo



