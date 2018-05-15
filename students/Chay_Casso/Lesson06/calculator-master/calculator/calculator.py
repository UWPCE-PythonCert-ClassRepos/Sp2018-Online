"""Performs calculations."""
from .exceptions import InsufficientOperands

class Calculator(object):
    """Performs calculations."""

    def __init__(self, adder, subtracter, multiplier, divider):
        """Initializes calculator using specified modules."""
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """Enters a number onto the stack."""
        self.stack.insert(len(self.stack), number)

    def _do_calc(self, operator):
        """Tries to perform the calculation method with two numbers."""
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands
        self.stack = [result]
        return result

    def add(self):
        """Adds two numbers."""
        return self._do_calc(self.adder)

    def subtract(self):
        """Subtracts two numbers."""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """Multiplies two numbers."""
        return self._do_calc(self.multiplier)

    def divide(self):
        """Subtracts two numbers."""
        return self._do_calc(self.divider)
