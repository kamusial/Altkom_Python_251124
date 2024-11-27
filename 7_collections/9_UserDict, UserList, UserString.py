from collections import UserDict, UserList, UserString

class MyDict(UserDict):
    def __setitem__ (self, key, value):
        print('Ustawienie {} na {}'.format(key, value))
        super().__setitem__(key, value)

md = MyDict()
md['a'] = 1
print(md)

class MyList(UserList):
    def append(self, item):
        print(f'dodawanie {item}')
        super().append(item)
        super().append(type(item))

ml = MyList()
ml.append(1)
print(ml)

class MyString(UserString):
    def __str__(self):
        return self.data.upper()

ms = MyString('hello')
print(ms)




