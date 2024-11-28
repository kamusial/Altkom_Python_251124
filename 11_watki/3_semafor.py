import threading
import random
import time

def worker(semaphore, worker_id):
    print(f'Worker {worker_id} czeka na dostęp do semaforu')
    with semaphore:
        print(f'worker {worker_id} zajął semafor')
        work_time = random.uniform(0.5, 2)
        time.sleep(work_time)
        print(f'Worker {worker_id} zwalnia semafor po {work_time}s')
    print(f'Worker {worker_id} zwolnił semafor')

semaphore = threading.Semaphore(2)

threads = []
for i in range (5):
    thread = threading.Thread(target=worker, args=(semaphore, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    print(thread.is_alive())
    thread.join(timeout=None)

print('Wszystko zakończone')