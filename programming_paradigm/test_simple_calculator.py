import unittest
from simple_calculator import SimpleCalculator


class TestCal(unittest.TestCase):
    def setUp(self):
        self.cal = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.cal.add(5, 5), 10)
        self.assertEqual(self.cal.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(5, 5), 0)
        self.assertEqual(self.cal.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(5, 5), 25)
        self.assertEqual(self.cal.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.cal.divide(10, 5), 2)
        self.assertIsNone(self.cal.divide(10, 0))


if __name__ == '__main__':
    unittest.main()
