import multiprocessing as mp
import time
import random

def producer(queue, n_items):
    for _ in range(n_items):
        item = random.randint(1, 100)
        print(f'Producing item {item}')
        queue.put(item)
        time.sleep(random.uniform(0.1, 0.5))
    queue.put(None)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consuming {item}')
        time.sleep(random.uniform(0.4, 1))

if __name__ == '__main__':
    queue = mp.Queue()
    n_items = 10
    producer_process = mp.Process(target=producer, args=(queue, n_items))
    consumer_process = mp.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print('Koniec')


