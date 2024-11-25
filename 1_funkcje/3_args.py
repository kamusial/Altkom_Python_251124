def license_confiscated(pesel, *penalties, surname='Kowalski'):
    if pesel not in pesel_list:
        print(f'Nie znaleziono numer pesel: {pesel}')
        return None
    total = 0
    for penalty in penalties:
        total += penalty
    if total > 600:
        print(f'License CONFISCATED from {surname}')
        return True
    return False

pesel_list = [1234, 2345, 3456, 4567, 5678]

print(license_confiscated(2345, 35, 200, 400))


