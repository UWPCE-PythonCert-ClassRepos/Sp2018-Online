"""Calculator"""


from .exceptions import InsufficientOperands


class Calculator(object):
    """
    calculator class
    add,subtract, multiply, and divide
    """
    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider
        self.stack = []

    def enter_number(self, number):
        """this is my method doc string"""
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """this is my method doc string"""
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """this is my method doc string"""
        return self._do_calc(self.adder)

    def subtract(self):
        """this is my method doc string"""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """this is my method doc string"""
        return self._do_calc(self.multiplier)

    def divide(self):
        """this is my method doc string"""
        return self._do_calc(self.divider)
