import threading
import time
import random
from order_manager import OrderManager
from order import Order

class Waiter(threading.Thread):
    def __init__(self, name, order_manager):
        super().__init__(name=name)
        self.order_manager = order_manager

    def run(self):
        for _ in range(5):
            time.sleep(random.uniform(0.5, 2))
            table_number = random.randint(1, 10)
            items = [f'item{random.randint(1, 10)}' for _ in range(1, 3)]
            order = Order(table_number, items)
            self.order_manager.add_order(order)
            print(f'{self.name} order {order}' )

