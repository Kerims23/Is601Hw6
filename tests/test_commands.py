'''testing commands'''
from decimal import Decimal
from calculator.plugins.addition.add_plugin import AddCommand
from calculator.plugins.division.division_plugin import DivideCommand

def test_add_command():
    '''add command'''
    command = AddCommand(Decimal('3'), Decimal('5'))
    assert command.execute() == Decimal('8')

def test_divide_command():
    '''divide command'''
    command = DivideCommand(Decimal('10'), Decimal('2'))
    assert command.execute() == Decimal('5')

def test_divide_by_zero():
    '''division error command'''
    command = DivideCommand(Decimal('10'), Decimal('0'))
    assert command.execute() == "Cannot divide by zero!"
