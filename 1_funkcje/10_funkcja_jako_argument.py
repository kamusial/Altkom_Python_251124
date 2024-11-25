people = [
    {"imie": "Anna", "wiek": 30, "zawod": "Inżynier"},
    {"imie": "Jan", "wiek": 40, "zawod": "Artysta"},
    {"imie": "Kasia", "wiek": 22, "zawod": "Programista"},
    {"imie": "Stefan", "wiek": 35, "zawod": "Inżynier"},
    {"imie": "Ewa", "wiek": 28, "zawod": "Architekt"}
]

# program filtrować
# program przetwarza / przedstawia
# operacje - pobrać imię    i    zwrócic opis

def filter_people(people, criterion):
    return [person for person in people if criterion(person)]

def use_people(people, operation):
    return [operation(person) for person in people]

# filers
def is_engineer(person):
    return person["zawod"] == "Inżynier"

def is_under_30(person):
    return person["wiek"] < 30

# operations
def get_name(person):
    return person['imie']

def description(person):
    return f"{person['imie']} ma {person['wiek']} lat i jest {person['zawod']}."

engineers = filter_people(people, is_engineer)
print(engineers)
print(f'Inżynierowie: {use_people(engineers, description)}')

under30 = filter_people(people, is_under_30)
print(f'osoby młodsze, niż 30 lat: {use_people(under30, get_name)}')