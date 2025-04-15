#https://github.com/adelvansoliman/lab10-AS-YD.git
# Partner 1: Adel-Van Soliman
# Partner 2: Yulee Donnelly
import unittest

import math

from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add():
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    def test_subtract():
        assert calculator.sub(5, 3) == 2
        assert calculator.sub(-1, -1) == 0
        assert calculator.sub(10, 20) == -10

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(5, 25), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(1, 100)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -5)
        with self.assertRaises(ValueError):
            logarithm(1, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()