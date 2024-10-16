'''divide command Imports Command from calculator.commands.command'''
from calculator.commands.command import Command
import logging

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            logging.error("division by zero error ")
            raise ZeroDivisionError("An error occurred: Cannot divide by zero")
        logging.info("exec division")
        return self.a / self.b

# def register():
#     return DivideCommand
