import unittest
from bank import KontoBankowe

class TestKontoBankowe(unittest.TestCase):
    def setUp(self):
        self.konto = KontoBankowe('jan Kowalski', 500)

    def test_inicjalizacja(self):
        self.assertEqual(self.konto.wlasciciel, 'Jan Kowalski')
        self.assertEqual(self.konto.saldo, 500)

    def test_wplata_poprawna(self):
        self.konto.wplata(500)
        self.assertEqual(self.konto.saldo, 1000)

    def test_wplata_bledna(self):
        with self.assertRaises(ValueError):
            self.konto.wplata(-100)

    def test_wyplata_poprawna(self):
        self.konto.wyplata(300)
        self.assertEqual(self.konto.saldo, 200)

    def test_wyplata_niewystarczajace_srodki(self):
        with self.assertRaises(ValueError):
            self.konto.wyplata(2000)

    def test_wyplata_bledna_kwota(self):
        with self.assertRaises(ValueError):
            self.konto.wyplata(-200)

    def test_sprawdz_saldo(self):
        self.assertEqual(self.konto.sprawdz_saldo(), 500)

if __name__ == '__main__':
    unittest.main()