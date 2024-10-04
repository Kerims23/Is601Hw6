"""Module to handle Calculation transactions."""

from calculator.calculation import Calculation

class Calculations:
    """Handles calculation history."""

    history = []

    @staticmethod
    def add_calculation(calculation: Calculation):
        """Add a calculation to the history."""
        Calculations.history.append(calculation)

    @staticmethod
    def get_history():
        """Return the full history."""
        return Calculations.history

    @staticmethod
    def clear_history():
        """Clear the history."""
        Calculations.history.clear()

    @staticmethod
    def get_latest():
        """Return the latest calculation."""
        return Calculations.history[-1] if Calculations.history else None
