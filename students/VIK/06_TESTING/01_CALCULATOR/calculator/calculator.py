"""
Module to create a custom Calculator class
"""

from .exceptions import InsufficientOperands

class Calculator(object):
    """
    Custom build calculator that soft-inherits operators (inside __init__) to perform calculation
    """

    def __init__(self, adder, subtracter, multiplier, divider):
        """
        Manual inherits stand alone class operators; adder, substracter... that have have a .calc to perform operation

        self.stack is initialized as a empty list that will hold values to perform operators on in memory

        :param adder: class to perform num1 + num2 via self.calc
        :param subtracter: class to perform num1 - num2 via self.calc
        :param multiplier: class to perform num1 * num2 via self.calc
        :param divider:  class to perform num1 / num2 via self.calc
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        adds a number to memory
        :param number: int or float
        :return: none
        """
        self.stack.append(number)

    def _do_calc(self, operator):
        """
        calls the .calc from the soft inherited operators
        :param operator: class instance, (soft inherited operators from __init__)
        :return: result, calculated operator performed on the two values in memory self.stack[0] and self.stack[1]
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        adder method that calls _do_calc (performs the self.adder.calc operation)
        :return: float
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        subtract method that calls _do_calc (performs the self.subtracter.calc operation)
        :return: float
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        multiply method that calls _do_calc (performs the self.multiply.calc operation)
        :return: float
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        divide method that calls _do_calc (performs the self.divide.calc operation)
        :return: float
        """
        return self._do_calc(self.divider)
