"""
A simple calculator module with basic mathematical operations.
"""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide the first number by the second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result