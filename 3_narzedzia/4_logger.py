from logging import *
# konfiguracja loggera
logger = getLogger(__name__)
logger.setLevel(INFO)
file_handler = FileHandler('Log.log')
console_handler = StreamHandler()
format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
formatter = Formatter(format)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        logger.info(f'Konto utworzone dla {self.owner} z saldem {self.balance}')

    def deposit(self, amount):
        if amount <= 0:
            logger.error('Kwota musi być większa od zera')
            raise ValueError('Kwota musi być większa od zera')
        self.balance += amount
        logger.info(f'Wpłata {amount} dla {self.owner}. Nowe saldo to {self.balance}')

    def withdraw(self, amount):
        if amount <= 0:
            logger.error("Kwota wypłaty musi być większa od zera")
            raise ValueError("Kwota wypłaty musi być większa od zera")
        if amount > self.balance:
            logger.error(f"Brak wystarczających środków dla wypłaty {amount} u {self.owner}")
            raise ValueError("Brak wystarczających środków")
        self.balance -= amount
        logger.info(f"Wypłata {amount} dla {self.owner}. Nowe saldo: {self.balance}")

    def get_balance(self):
        logger.info(f"Sprawdzenie salda dla {self.owner}: {self.balance}")
        return self.balance

# Testowanie programu
import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Tworzenie nowego konta przed każdym testem
        self.account = BankAccount("Jan Kowalski", 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0)

    def test_withdraw(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.get_balance(), 700.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500.0)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100.0)

if __name__ == "__main__":
    # Uruchomienie testów
    unittest.main()