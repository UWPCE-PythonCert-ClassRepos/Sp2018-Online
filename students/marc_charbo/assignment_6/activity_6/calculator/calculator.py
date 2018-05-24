"""
calculator module
"""

from .exceptions import InsufficientOperands

class Calculator(object):
    """ class manages calculator stack and all its operations"""

    def __init__(self, adder, subtracter, multiplier, divider):
        """
        :param adder: adder class object
        :param subtracter: subtracter class object
        :param multiplier: multiplier class object
        :param divider: divider class object
        :param stack: stores numbers and results
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider
        self.stack = []

    def enter_number(self, number):
        """
        :param number: appends number to end stack
        :return: nothing
        """
        self.stack.append(number)  # changed insert to append

    def _do_calc(self, operator):
        """
        :param operator: performs calc method on operator object (add, sub, div, multi)
        :return: returns results of calc
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        :return: calls do_calc on adder
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        :return: calls do_calc on substract
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        :return:  calls do_calc on multiply
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        :return: calls do_calc on divide
        """
        return self._do_calc(self.divider)
