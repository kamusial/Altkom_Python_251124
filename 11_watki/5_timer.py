import threading

def delayed_function():
    print(f'Start funkcji')

timer = threading.Timer(3, delayed_function)
timer.start()


