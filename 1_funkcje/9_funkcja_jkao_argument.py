def square(x):
    return x * x

def double(x):
    return x * 2

def apply(list, function):
    return [function(x) for x in list]

numbers = [1, 2, 3, 4, 5]
result = apply(numbers, square)

print(result)