"""
This module provides a calculator class for operating on pairs of operands.
"""
from .exceptions import InsufficientOperands


class Calculator(object):
    """
    This class provides a way to perform operations on two operands.
    """

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        This method enables the user to add numbers to the calculator stack.
        """
        self.stack.append(number)

    def _do_calc(self, operator):
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        This method calls the adder method from the Adder class
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        This method calls the subtractor method from the Subtractor class
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        This method calls the multiplier method from the Multiplier class
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        This method calls the divider method from the Divider class
        """
        return self._do_calc(self.divider)
