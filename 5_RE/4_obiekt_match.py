import re

text = "The rain in Spain falls mainly in the plain."
pattern = r'\b\w*ain\b'
match = re.search(pattern, text)
if match:
    print(f'dopasownay tekst: {match.group()}')
    print(f'pozycja początku: {match.start()}')
    print(f'pozycja końca: {match.end()}')
    print(f'zakres: {match.span()}')
else:
    print('brak')