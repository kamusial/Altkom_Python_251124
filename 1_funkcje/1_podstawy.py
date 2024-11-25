def mnozenie(a, b=3, c=4):
    return a * b * c


def pokaz_3ci_element(nazwa: str) -> str:
    return nazwa[2]

print(mnozenie(3, 5))
print(mnozenie(3, 'pies'))

moja_lista = [1, 2, 3, 4, 5, 6, 7]
print(pokaz_3ci_element(moja_lista))