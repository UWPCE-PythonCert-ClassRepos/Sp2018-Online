""" Calculator module """
from .exceptions import InsufficientOperands


class Calculator(object):
    """ Calculator class """

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """ Takes input as a number and inserts into a stack """
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """ Performs the calculation operation on inserted numbers in stack """
        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """ Add operation on numbers in stack """
        return self._do_calc(self.adder)

    def subtract(self):
        """ Subtract operation on numbers in stack """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """ Multiply operation on numbers in stack """
        return self._do_calc(self.multiplier)

    def divide(self):
        """ Divide operation on numbers in stack """
        return self._do_calc(self.divider)
