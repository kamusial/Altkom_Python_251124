import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread1.start()

for i in range(5, 10):
    print(i)
    time.sleep(1)

thread1.join()