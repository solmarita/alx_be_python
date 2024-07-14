import unittest
from simple_calculator import SimpleCalculator

calc = SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase):
    def test_simplecalculator_add(self):
        result = calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_simplecalculator_subtract(self):
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_simplecalculator_multiply(self):
        result = calc.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_simplecalculator_divide(self):
        result = calc.divide(15, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
  unittest.main()