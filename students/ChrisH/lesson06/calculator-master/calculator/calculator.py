"""
Module that implements a simple calculator.
CLASSES
    Calculator(object)
        stack - list of numbers maintained as LIFO stack
        add()
        subtract()
        mulitiply()
        divide()
"""

from .exceptions import InsufficientOperands


class Calculator(object):
    """
    Class implementing a Calculator object
    :return: Result of operation
    """
    def __init__(self, adder, subtracter, multiplier, divider):
        """Initialization for class object"""
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """Inserts number into stack"""
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """Executes calc statement of a given class object"""
        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """Add function"""
        return self._do_calc(self.adder)

    def subtract(self):
        """Subtract function"""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """Multiply function"""
        return self._do_calc(self.multiplier)

    def divide(self):
        """divide function"""
        return self._do_calc(self.divider)
