import threading
import time

event = threading.Event()

def waiter():
    print('Czekam na zdarzenie')
    event.wait()
    print('Zdarzenie ustawione')

def setter():
    time.sleep(2)
    event.set()
    print('Zdarzenie ustawione przez setter\n')

waiter_thread = threading.Thread(target=waiter)
setter_thread = threading.Thread(target=setter)

waiter_thread.start()
setter_thread.start()

waiter_thread.join()
setter_thread.join()