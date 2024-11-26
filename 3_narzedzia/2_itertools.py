import itertools

# Nieskończony licznik zaczynający się od 10
for i in itertools.count(10):
    if i > 20:
        break
    print(i)

# Powtorz elementy listy nieskonczenie wiele razy
licznik = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if licznik > 10:
        break
    print(item)
    licznik += 1

# generowanie wszystkich mozliwych permutacji
for p in itertools.permutations(['A', 'B', 'C']):
    print(p)

# generowanie kombinacji 2-elementowych z listy
for c in itertools.combinations(['A', 'B', 'C'], 2):
    print(c)

for c in itertools.combinations_with_replacement(['A', 'B', 'C'], 2):
    print(c)

# łączenie list w jedną sekwencję
for item in itertools.chain(['A', 'B', 'C'], [1,2,3]):
    print(item, end=' ')

print(list(itertools.chain.from_iterable(['1', '2', ['3', '4', '5'], ['A', 'B', 'C']])))

# grupowanie elementów wg dlugości
data = ['abc', 'de','fgh', 'i', 'sdfg']
for k, g in itertools.groupby(data, key=len):# grupow
    print(f'Klucz: {k}, Grupa: {list(g)}')
