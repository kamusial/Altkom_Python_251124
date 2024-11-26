import re

pattern = r'ab*c'
text = 'Kamil ac, abc, Kamil, abbbc'
matches = re.findall(pattern, text)
print(matches)

text = "The rain in Spain falls mainly in the plain."
# znaleźć wszystkie słowa kończące się na 'ain'
pattern = r'\b\w*ain\b'
matches = re.findall(pattern, text)
print(matches)

text = 'Kamil i komputer. Kamil i Zbyszek się znają'
# znaleźć wszystkie słowa zaczynające sie na wielką literę
pattern = r'\b[A-Z]\w*\b'
matches = re.findall(pattern, text)
print(matches)

text = "Kontakt: +48 123 456 789, 0048-123-456-789, (48) 123-456-789."
# znaleźć numery kierunkowe w różnych formatach
pattern = r'(\+?\d{1,4}[-\s]?|\(\d{1,4}\)[-\s]?)?\d{3}[-\s]?\d{3}[-\s]?\d{3}'
matches = re.findall(pattern, text)
print(matches)

text = "Wydarzenia: 12-05-2020, 23-08-2019, oraz 01-01-2021."
pattern = r'(\d{2})-(\d{2})-(\d{4})'
matches = re.findall(pattern, text)
for day, month, year in matches:
    print(f'Dzien: {day}, miesiac: {month}, rok: {year}')

text = 'Fragment Apiosenki Ao psie, który jezdził koleją'
# słowa, zaczynające się na A i mające minimum 4 znaki
pattern = r'\bA\w{3,}\b'
matches = re.findall(pattern, text)
print(matches)