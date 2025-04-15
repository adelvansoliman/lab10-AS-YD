"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
import unittest
from calculator import *

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return a / b

def logarithm(a, b):
  if a <= 0 or b <= 1:
    raise ValueError("Domain error: base must be > 1 and number must be > 0")
  return math.log(a, b)

def exponent(a, b):
  return a ** b

def square_root(a):
    if a < 0:
      raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
  return math.hypot(a, b)

class TestCalculator(unittest.TestCase):

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


if __name__ == '__main__':
  unittest.main()