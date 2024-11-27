from collections import UserDict

class TrackedDict(UserDict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.access_count = {}

    def __getitem__(self, key):
        print(f'Odczytanie klucza {key}')
        self.access_count[key] = self.access_count.get(key, 0) + 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print(f'Zapis wartości {value} dla klucza {key}')
        self.access_count[key] = self.access_count.get(key, 0) + 1
        super().__setitem__(key, value)

    def get_access_count(self, key):
        return self.access_count.get(key, 0)

td = TrackedDict()

td['a'] = 1
td['b'] = 2
print(td['a'])
td['a'] = 3
print(td['b'])
print(td['a'])

print(f"Liczba operacji na kluczu 'a': {td.get_access_count('a')}")
print(f"Liczba operacji na kluczu 'b': {td.get_access_count('b')}")


