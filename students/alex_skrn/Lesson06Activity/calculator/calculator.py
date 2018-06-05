#!/usr/bin/env python3
"""This modules provides a class for creating a calculator object."""

from .exceptions import InsufficientOperands


class Calculator(object):
    """Provide the calculator class."""

    def __init__(self, adder, subtracter, multiplier, divider):
        """Instantiate with instances of operators, create a memory stack."""
        # See "depencency inversion," "depencency injection"
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        # A kind of a calculator memory
        self.stack = []

    def enter_number(self, number):
        """Provide a method to enter numbers into the calculator memory."""
        # self.stack.insert(0, number) # OLD
        self.stack.append(number)

    def _do_calc(self, operator):
        """Apply operator to first two numbers on stack and return the result.

        Updates the stack by repalcing its content with the result.
        Raises InsufficientOperands exception if not enough operands.
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        # Clear the stack and set the result into the stack
        self.stack = [result]
        return result

    def add(self):
        """Provide a method to do addition if the stack has 2 operands."""
        return self._do_calc(self.adder)

    def subtract(self):
        """Provide a method to do subtraction if the stack has 2 operands."""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """Provide a method to do multiplication if stack has 2 operands."""
        return self._do_calc(self.multiplier)

    def divide(self):
        """Provide a method to do division if the stack has 2 operands."""
        return self._do_calc(self.divider)
