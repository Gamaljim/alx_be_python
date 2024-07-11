import unittest
from simple_calculator import SimpleCalculator


class TestCal(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 5), 10)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == '__main__':
    unittest.main()
