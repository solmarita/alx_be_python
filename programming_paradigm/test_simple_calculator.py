import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    self.assertEqual(self.calc.add
    self.assertEqual(self.calc.subtract
    self.assertEqual(self.calc.multiply
    self.assertEqual(self.calc.divide
    test_multiplication(self)
    SimpleCalculator()
    """

    def test_addition(self):
        result = SimpleCalculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = SimpleCalculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = SimpleCalculator.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = SimpleCalculator.divide(15, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
  unittest.main()