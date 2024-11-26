import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Rozpoczynam dzialanie funkcji {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Czas wykonania {end_time - start_time:.5f}s')
        return result
    return wrapper

@time_decorator
def opoznienie(n):
    time.sleep(n)
    print('Funkcja zakończona!')
    return n * 2

result = opoznienie(5)
print(f'Wynik funkcji {result}')
