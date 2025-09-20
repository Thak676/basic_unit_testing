"""
Unit tests for the calculator module.
"""

import unittest
from calculator import add, subtract, multiply, divide, is_even, factorial


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(2.5, 1.5), 4.0)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test the divide function."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-6, 3), -2.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)
        with self.assertRaises(ValueError):
            divide(-5, 0)

    def test_is_even(self):
        """Test the is_even function."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))

    def test_factorial(self):
        """Test the factorial function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        """Test that factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)


if __name__ == '__main__':
    unittest.main()