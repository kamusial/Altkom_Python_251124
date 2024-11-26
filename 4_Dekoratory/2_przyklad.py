import functools

def dekorator_logujący(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Wywołanie funkcji {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Zakończenie funkcji {func.__name__}')
        return result
    return wrapper

### SPRAWDZIĆ LOGOWANIE FUNKCJI WRAPPER

def dekorator_zabezpieczający(func):
    def wrapper(dzielna, dzielnik):
        print('Sprawdzam parametry')
        if dzielnik == 0:
            print(f'Blad, dzielenie przez zero')
            raise ValueError ('Błąd, dzielenie przez zero')
        return func(dzielna, dzielnik)
    return wrapper

@dekorator_logujący
@dekorator_zabezpieczający
def dzielenie(a, b):
    return a / b

@dekorator_logujący
def dodawanie(a, b):
    return a + b


print(dodawanie(3, 5))

try:
    print(dzielenie(3, 0))
except ValueError as e:
    print(e)