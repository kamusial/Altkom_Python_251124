import threading

lock = threading.Lock()
def thread_task():
    with lock:
        # sekcja krytyczna
        pass

rlock = threading.RLock()
with rlock:
    pass


counter = 0
lock = threading.Lock()
def increment():
    global counter
    with lock:
        counter += 1

rlock = threading.RLock()

def outer_function():
    with rlock:
        print('Outer function')
        inner_function()

def inner_function():
    with rlock:
        print('Inner function')

outer_function()