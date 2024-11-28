from order_manager import OrderManager
from waiter import Waiter
from chef import Chef

def main():
    order_manager = OrderManager()
    waiters = [Waiter(f'Kelner-{i}', order_manager) for i in range(3)]
    chefs = [Chef(f'Kucharz-{i}', order_manager) for i in range(2)]

    for waiter in waiters:
        waiter.start()
    for chef in chefs:
        chef.start()

    for waiter in waiters:
        waiter.join()
    for chef in chefs:
        chef.join(timeout=1)

if __name__ == '__main__':
    main()