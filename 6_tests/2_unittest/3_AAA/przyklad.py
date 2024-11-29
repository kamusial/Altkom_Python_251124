import unittest

class Calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def test_add(self):
#        self.assertEqual(Calculator().add(1, 2), 3)
        # Arrange
        calculator = Calculator()
        a = 5
        b = 3

        # Act
        result = calculator.add(a, b)

        # Assert
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()