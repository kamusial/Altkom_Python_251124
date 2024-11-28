class Order:
    def __init__(self, table_number, items):
        self.table_number = table_number
        self.items = items

    def __repr__(self):
        return f'Zamowienie (table={self.table_number}, items={self.items})'



