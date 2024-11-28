import multiprocessing as mp
import time
import random

def square(n):
    print(f'Proces {mp.current_process().name}: liczy pole z {n}')
    time.sleep(random.randint(1, 5))
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with mp.Pool(processes=4) as pool:
        result= pool.map(square, numbers)
    print(result)
