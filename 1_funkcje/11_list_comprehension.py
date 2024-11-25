from pydoc import describe

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

words = ['jablko', 'banan', 'piesek', 'kot']
lenghts = [len(word) for word in words]
print(lenghts)

list_of_lists = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
flat_list = [element for sublist in list_of_lists for element in sublist]
print(flat_list)

grades = [2, 3, 6, 5, 8, 9, 3, 7, 5]
description = ['mala' if grade <= 4 else 'duza' for grade in grades]
print(description)

# Chcemy utworzyć listę zawierającą kwadraty liczb parzystych
# z zakresu od 1 do 20, które są większe niż 50, a następnie
# podzielić każdy z nich przez 2. Ostatecznie lista ma zawierać
# wyniki w formacie (oryginalna liczba, przekształcona wartość).

result = [(x, (x ** 2) / 2) for x in range (1, 21) if x % 2 == 0 and x ** 2 > 50]
print(result)

