import functools
import time
def cache_decorator(func):
    cache = {}
    #@functools.wraps(func)
    def wrapper(*args, **kwargs):
        # klucz cache na podstawie argumentow
        cache_key = args + tuple(kwargs.items())

        # logowanie
        print(f'Funkcja {func.__name__} z {args} i {kwargs}')
        if cache_key in cache.keys():
            print(f'Uzywam wartości z cashe')
            return cache[cache_key]

        # pomiar czasu
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f'Czas trwania {duration:.5f}s')

        # zapisanie wyniku w cashe
        cache[cache_key] = result
        return result
    return wrapper

@cache_decorator
def dluga_operacja(x, y):
    time.sleep(3)
    return x * y + x / y

print(dluga_operacja(2, 3))
print(dluga_operacja(3, 3))
print(dluga_operacja(2, 3))
