from kod import fizzbuzz
import pytest

def test_1():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '2'
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(4) == '4'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'

def test_2():
    assert fizzbuzz(0) == None
    assert fizzbuzz(-5) == None

def test_3():
    assert fizzbuzz(2.7) == '2'
    assert fizzbuzz(3.1) == 'Fizz'
    assert fizzbuzz(3.9) == 'Fizz'
    assert fizzbuzz(15.1) == 'FizzBuzz'

def test_4():
    assert fizzbuzz('mama') == None


