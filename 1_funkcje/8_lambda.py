def add(x, y):
    return x + y

dodaj = lambda x, y: x + y

result = dodaj(5, 3)
print(result)

square = lambda x: x ** 2

# sortowanie krotek
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

def multipier(n):
    return lambda x: x * n

double = multipier(2)
triple = multipier(3)

print(double(10))
print(triple(4))

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x+1, numbers))
print(result)

