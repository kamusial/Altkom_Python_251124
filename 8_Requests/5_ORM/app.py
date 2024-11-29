from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Uzytkownik, Zamowienie

# Tworzenie silnika
engine = create_engine('sqlite:///orders.db')

# Tworzenie wszystkich tabel
Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()


uzytkownik1 = Uzytkownik(imie='Kamil', nazwisko='Musial', email='kamil@altkom.com')
uzytkownik2 = Uzytkownik(imie='Anna', nazwisko='Nowak', email='ania@wp.pl')

session.add(uzytkownik1)
session.add(uzytkownik2)
session.commit()

zamowienie1 = Zamowienie(opis='Laptop', uzytkownik=uzytkownik1)
zamowienie2 = Zamowienie(opis='PC', uzytkownik=uzytkownik1)
session.add(zamowienie1)
session.add(zamowienie2)
session.commit()

#pobieranire wszystkich uzytkowników
uzytkownicy = session.query(Uzytkownik).all()
for uzytkownik in uzytkownicy:
    print(uzytkownik)

#filtrowanie danych
kamil = session.query(Uzytkownik).filter_by(imie='Kamil').first()
print(kamil)

#pobieranie zamowień uzytkownika
zamowienia_kamila = kamil.zamowienia
for zamowienie in zamowienia_kamila:
    print(zamowienie)

# aktualizacja maila
kamil.email = 'kamil21@wp.pl'
session.commit()

# usuwanie zamówienia
session.delete(zamowienie1)
session.commit()

# zaawansowane zapytanie
from sqlalchemy.orm import joinedload
uzytkownicy_z_zamowieniami = session.query(Uzytkownik).options(joinedload(Uzytkownik.zamowienia)).all()
for uzytkownik in uzytkownicy_z_zamowieniami:
    print(f"{uzytkownik.imie} zamówił:")
    for zamowienie in uzytkownik.zamowienia:
        print(f" - {zamowienie.opis}")

session.close()