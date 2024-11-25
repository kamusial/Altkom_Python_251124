def advanced_function(*args, **kwargs):

    if not args:
        raise ValueError('Potrzebna przynajmniej jedna liczba')
    operation = kwargs.get('operation', 'sum')
    filter_type = kwargs.get('filter', None)
    threshold = kwargs.get('threshold', None)

    # Filtrowanie liczb
    numbers = list(args)
    if filter_type == 'even':
        numbers = [n for n in numbers if n % 2 == 0]
    elif filter_type == 'odd':
        numbers = [n for n in numbers if n % 2 != 0]

    # Filtrowanie wg produ
    if threshold is not None:
        numbers = [n for n in numbers if n >= threshold]

    # Czy po filtrowaniu zostaly liczby
    if not numbers:
        raise ValueError('Zadne liczby nie spelniają kryterium')

    # Operacje
    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'multiplication':
        result = 1
        for n in numbers:
            result *= n
    elif operation == 'avg':
        result = sum(numbers)/len(numbers)
    else:
        raise ValueError(f'Nieznan operacja {operation}')
    return result

print(advanced_function(1, 2, 3, 4, operation='sum'))
print(advanced_function(1, 2, 3, filter='even', threshold=2))
print(advanced_function(1, 2, 3, 4, 5, 6, 7, threshold=2, operation='multiplication'))
print(advanced_function(1, 2, 3, 4, 5, 6, 7, threshold=10, operation='multiplication'))