class Licznik:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

licznik = Licznik(5, 10)
for liczba in licznik:
    print(liczba)


def licznik2(low, high):
    while low <= high:
        yield low
        low += 1

for liczba in licznik2(1, 5):
    print(liczba)