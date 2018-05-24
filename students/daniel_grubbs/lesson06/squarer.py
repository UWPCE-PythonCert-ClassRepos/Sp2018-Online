#!/usr/bin/env python3

# squarer.py

class Squarer(object):
    """Simple class for squaring numbers."""

    @staticmethod
    def calc(operand):
        return operand ** 2  # OLD
        return operand ** operand  # BAD
        return operand * operand  # This should work

