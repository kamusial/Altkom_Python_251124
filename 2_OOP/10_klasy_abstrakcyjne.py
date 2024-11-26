from abc import ABC, abstractmethod


class Pojazd(ABC):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    @abstractmethod
    def uruchom(self):
        pass

    @abstractmethod
    def zatrzymaj(self):
        pass

class Samochod(Pojazd):
    def uruchom(self):
        print(f"Samochód {self.marka} {self.model} uruchomiony.")

    def zatrzymaj(self):
        print(f"Samochód {self.marka} {self.model} zatrzymany.")


class Motocykl(Pojazd):
    def uruchom(self):
        print(f"Motor {self.marka} {self.model} uruchomiony.")

    def zatrzymaj(self):
        print(f"Motor {self.marka} {self.model} zatrzymany.")

samochod = Samochod(marka="Toyota", model="Yaris")
samochod.uruchom()
samochod.zatrzymaj()

motocykl = Motocykl(marka="Harley", model="Best")
motocykl.uruchom()