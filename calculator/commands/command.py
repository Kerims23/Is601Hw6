''' Contains the base Command class'''
import logging

class Command:
    def __init__(self, a, b):
        '''init'''
        self.a = a
        self.b = b
        logging.info("init command.py")

    def execute(self):
        '''execute '''
        raise NotImplementedError("Subclasses should implement this method.")
