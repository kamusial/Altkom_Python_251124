import re

pattern = r'abc'
text = 'xyzabcdef'
match = re.search(pattern, text)
if match:
    print(match.group())

pattern = r'ab+c'
text = r' Kamil i Pythonabbbc i juz'
match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print('No match')



text = "Uwielbiam programowanie w Pythonie!"
pattern = r"Python"

# Szukanie pierwszego dopasowania
result = re.search(pattern, text)

if result:
    print("Znaleziono wzorzec:", result.group())
else:
    print("Wzorzec nie został znaleziony")

