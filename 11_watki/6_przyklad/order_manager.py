from order import Order
from collections import deque
import threading
import time
import random

class OrderManager:
    def __init__(self):
        self.orders = deque()
        self.order_event = threading.Event()
        self.lock = threading.Lock()

    def add_order(self, order):
        with self.lock:
            self.orders.append(order)
            print(f'zamowienie dodane: {order}')
        self.order_event.set()

    def get_orders(self):
        while True:
            self.order_event.wait()
            with self.lock:
                if self.orders:
                    order = self.orders.popleft()
                    if not self.orders:
                        self.order_event.clear()
                    return order
            self.order_event.clear()

