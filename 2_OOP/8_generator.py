def generator_potraw():
    yield 'Starter: pomidorowa'
    yield 'Główne: Schabowy'
    yield 'Deser: ciastko'
    yield 'Picie: Kawa'

potrawa = generator_potraw()

for danie in potrawa:
    print (danie)