from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Uzytkownik(Base):
    __tablename__ = 'uzytkownicy'

    id = Column(Integer, primary_key=True)
    imie = Column(String)
    nazwisko = Column(String)
    email = Column(String)

    zamowienia = relationship("Zamowienie", back_populates="uzytkownik")

    def __repr__(self):
        return f'Uzytkownik(imie={self.imie}) {self.nazwisko}'

class Zamowienie(Base):
    __tablename__ = 'zamowienia'

    id = Column(Integer, primary_key=True)
    opis = Column(String)
    uzytkownik_id = Column(Integer, ForeignKey('uzytkownicy.id'))

    uzytkownik = relationship("Uzytkownik", back_populates="zamowienia")

    def __repr__(self):
        return f'Zamowienie(opis={self.opis})'

