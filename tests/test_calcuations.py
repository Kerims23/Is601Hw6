"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from faker import Faker
from calculator.calculation import Calculation
from calculator.plugins.addition.add_plugin import AddCommand
#from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
#from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand

fake = Faker()

@pytest.fixture(params=[1, 10, 100])  # You can customize this list
def records(request):
    '''docstring to help with the num_records'''
    return request.param

def test_calculation_operations(a, b, operation, expected):
    """Test calculation operations."""
    calc = Calculation(a, b, operation)
    result = calc.perform()
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError):
            print(result)
    else:
        assert result == expected

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), AddCommand)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, AddCommand)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError.
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ZeroDivisionError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), DivideCommand)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ZeroDivisionError, match="An error occurred: Cannot divide by zero"):  # Expect ZeroDivisionError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ZeroDivisionError.
        