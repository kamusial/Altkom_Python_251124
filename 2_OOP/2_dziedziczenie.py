class Vehicle:
    def __init__ (self, brand, model, year, ID):
        self.brand = brand
        self.model = model
        self.year = year
        self.ID = ID

    def __str__(self):
        return f'Pojazd to {self.brand} {self.model} {self.ID}'

    def turn_on_engine(self):
        return f'Silnik w {self.model} uruchomiony'

class Car(Vehicle):
    def __init__(self, brand, model, year, ID, no_of_doors):
        super().__init__(brand, model, year, ID)
        self.no_of_doors = no_of_doors

    def __str__(self):
        return f'No po prostu auto'

class Bike(Vehicle):
    def __init__(self, brand, model, year, ID, engine):
        super().__init__(brand, model, year, ID)
        self.engine = engine

vehicle1 = Vehicle('Toyota', 'Yaris', 1999, 123)
print(vehicle1)

car1 = Car('Skoda', 'Fabia', 2014, 456, 4)
print(car1)
