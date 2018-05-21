"""
Module that defines a Adder operator class with Adder.calc to perform the calculation
"""

class Adder(object):
    """
    Class that used to feed the Calculator module __init__
    """
    @staticmethod
    def calc(operand_1, operand_2):
        """
        Method, adds args
        :param operand_1: int or float
        :param operand_2: int or float
        :return: float
        """
        return operand_1 + operand_2
