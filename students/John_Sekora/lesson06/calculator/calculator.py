"""
This module performs calculations
"""

from .exceptions import InsufficientOperands


class Calculator(object):
    """
    This class performs calculation methods
    """
    def __init__(self, adder, subtracter, multiplier, divider):
        """
        This method initializes variables
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        This method enters a number to the stack
        """
        if self.stack == []:
            self.stack.insert(0, number)
        else:
            self.stack.insert(1, number)

    def _do_calc(self, operator):
        """
        This method performs the calculation to the stack
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        This method performs addition
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        This method performs subtraction
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        This method performs multiplication
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        This method performs division
        """
        return self._do_calc(self.divider)
