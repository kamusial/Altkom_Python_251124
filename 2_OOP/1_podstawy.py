class Auto:

    def __init__(self, color, petrol_level=0, production_year=2025):
        self.color = color
        self.petrol_level = petrol_level
        self.condition = 5
        self.eco_mode = False
        self.petrol_consumption = 14
        self.age = 2024 - production_year
        self.car_active = True

    def __str__(self):
        return f'Auto ma kolor {self.color} i kondycje {self.condition}'

    def range(self):
        my_range = round(self.petrol_level / self.petrol_consumption * 100 * 0.9)
        return my_range

    def set_mode(self, mode):
        if mode == 'eco':
            self.eco_mode = True
            self.petrol_consumption = 9
        elif mode == 'normal':
            self.eco_mode = False
            self.petrol_consumption = 14
        else:
            print('Tryb nierozpoznany')

    def update_petrol_level(self, no_of_litters, refueling=False):
        if not refueling:
            if no_of_litters <= self.petrol_level:
                self.petrol_level -= no_of_litters
            else:
                print('Niedozwolona operacja')
        else:
            passwd = input('Podaj haslo: ')
            if passwd == '1234':
                self.petrol_level += no_of_litters


vehicle12 = Auto('blue', 50, 2012)
print(vehicle12.color)
vehicle12.color = 'red'
print(vehicle12.color)
print(vehicle12)
print(vehicle12.range())
vehicle12.update_petrol_level(20)
print(vehicle12.petrol_level)
