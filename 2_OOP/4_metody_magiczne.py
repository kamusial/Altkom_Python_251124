class Auto:
    def __init__(self, brand, year, condition):
        self.brand = brand
        self.year = year
        self.condition = condition

    def __str__(self):
        return f'{self.brand} - {self.year} - {self.condition}'

    def __eq__(self, other):
        return abs(self.year - other.year) <= 1 and self.condition == other.condition

    #    def __add__(self, other):   # dodawanie
    #    def __sub__(self, other):   # odejmowanie
    #    def __mul__(self, other):   # mnozenie
    #    def __len__(self):          # dlugosc

auto1 = Auto('Toyota', 1998, 4)
auto2 = Auto('BMW', 1999, 4)
print(auto1 == auto2)
        

