""" calculator module"""


from .exceptions import InsufficientOperands


class Calculator(object):
    """ calculator class """

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """ add number to the stack method """
        # insert at the end of the stack.
        self.stack.insert(len(self.stack), number)

    def _do_calc(self, operator):
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """ add method """
        return self._do_calc(self.adder)

    def subtract(self):
        """ subtract method """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """ multiply method """
        return self._do_calc(self.multiplier)

    def divide(self):
        """ divide method """
        return self._do_calc(self.divider)
