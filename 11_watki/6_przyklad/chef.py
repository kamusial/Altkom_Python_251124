import  threading
import time
from order_manager import OrderManager
import random

class Chef(threading.Thread):
    def __init__(self, name, order_manager):
        super().__init__(name=name)
        self.order_manager = order_manager

    def run(self):
        while True:
            order = self.order_manager.get_orders()
            if order:
                print(f'{self.name} przygotowuje {order}')
                time.sleep(random.randint(1, 3))
                print(f'{self.name} skończył zamówienie {order}')

