"""Operations for the calculator."""

from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Return the difference between two numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Return the product of two numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Return the division of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
