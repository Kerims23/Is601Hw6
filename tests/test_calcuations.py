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
from calculator.calculation import Calculation
from calculator.plugins.addition.add_plugin import AddCommand
#from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
#from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.

def generate_test_cases(num_records):
    '''generating test cases '''
    test_cases = []
    for i in range(num_records):
        a = Decimal(i + 1)
        b = Decimal(i + 2) if i < num_records - 1 else Decimal('0')  # Last case for zero division
        test_cases.append((a, b, DivideCommand, a / b if b != 0 else "An error occurred: Cannot divide by zero"))
    return test_cases

@pytest.mark.parametrize("num1, num2, operation, expected_result", generate_test_cases(100))
def test_calculation_operations(num1, num2, operation, expected_result):
    """Test various operations using the Calculation class."""
    calc = Calculation(num1, num2, operation)
    if expected_result == "An error occurred: Cannot divide by zero":
        with pytest.raises(ZeroDivisionError, match=expected_result):
            calc.perform()
    else:
        result = calc.perform()
        assert result == expected_result


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
        