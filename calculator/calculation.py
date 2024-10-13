"""Module to handle Calculation operations."""

from decimal import Decimal
from calculator.plugins.addition.add_plugin import AddCommand
from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand
import logging 
import logging.config 

class Calculation:
    """Handles a single calculation."""

    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def __repr__(self):
        # Assuming operation is a function, we use its name for representation
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
    
    def perform(self) -> Decimal:
        """Performs the operation."""
        command = self.operation(self.a, self.b)  # Create the command instance
        return command.execute() 

    @staticmethod
    def create(a: Decimal, b: Decimal, operation):
        """Factory method to create a new Calculation."""
        return Calculation(a, b, operation)
