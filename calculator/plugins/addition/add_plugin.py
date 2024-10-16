'''add command Imports Command from calculator.commands.command '''
from calculator.commands.command import Command
import logging

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        logging.info("execute addition")        
        return self.a + self.b

# def register():
#     return AddCommand
