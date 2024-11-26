class Zwierze:
    def dzwiek(self):
        raise NotImplementedError('Brak metody')


class Pies(Zwierze):
    def dzwiek(self):
        return 'Hau'


class Kot(Zwierze):
    def dzwiek(self):
        return 'Mial'


kot = Kot()
print(kot.dzwiek())

def odglos(zwierze: Zwierze):
    print(zwierze.dzwiek())

odglos(Pies())
odglos(Kot())