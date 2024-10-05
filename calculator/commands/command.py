''' Contains the base Command class'''
class Command:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError("Subclasses should implement this method.")
