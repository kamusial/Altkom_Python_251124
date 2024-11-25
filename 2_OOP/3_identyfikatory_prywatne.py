class Worker:
    def __init__(self, position, pesel):
        self.position = position
        self.__pesel = pesel

    def __str__(self):
        return f'{self.position}'

    def show_pesel(self, passwd):
        if passwd == 'Gabrysia':
            print(f'Pesel to {self.__pesel}')

    def change_pesel(self, new_pesel, passwd):
        if passwd == 'Gabrysia':
            self.__pesel = new_pesel
            print(f'new pesel to {self.__pesel}')


worker1 = Worker('engineer', '1234')
print(worker1)

# print(worker1.__pesel)
worker1.__pesel = '6789'
print(worker1)
worker1.show_pesel('Gabrysia')
worker1.change_pesel('Gabrysia', 'Gabrysia')
worker1.show_pesel('Gabrysia')