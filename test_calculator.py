#https://github.com/adelvansoliman/lab10-AS-YD.git
# Partner 1: Adel-Van Soliman
# Partner 2: Yulee Donnelly
import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(10, 20), -10)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(6, 2), 3)
        self.assertEqual(div(-10, 5), -2)
        self.assertEqual(div(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2, places=7)
        self.assertAlmostEqual(logarithm(2, 8), 3, places=7)
        self.assertAlmostEqual(logarithm(5, 25), 2, places=7)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == "__main__":
    unittest.main()