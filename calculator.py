"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

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
