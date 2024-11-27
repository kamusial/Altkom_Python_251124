from functions import mnozenie
import pytest

def test_mnozenie_basic():
    assert mnozenie(2, 3) == 6
    assert mnozenie(8, 3) == 24
    assert mnozenie(0, 3) == 0
    assert mnozenie(0, 0) == 0
    assert mnozenie(0, 1) == 0
    assert mnozenie(9, -2) == -18
    assert mnozenie(3, 0) == 0

def test_mnozenie_advanced():
    assert mnozenie(100, 1.1) == 110
    assert mnozenie(2, 1.1) == 2.2
    assert mnozenie(0.1, 0.002) == 0.0002
    assert mnozenie(0.001, 0.002) == 0.000002
    assert mnozenie('piesek', 2) == None
