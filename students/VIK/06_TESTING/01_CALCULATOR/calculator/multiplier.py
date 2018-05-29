"""
Module that defines a Multiplier operator class with Multiplier.calc to perform the calculation
"""

class Multiplier(object):
    """
    Class that used to feed the Calculator module __init__
    """
    @staticmethod
    def calc(operand_1, operand_2):
        """
        Method, multiplies 2 args
        :param operand_1: int or float
        :param operand_2: int or float
        :return: float
        """
        return operand_1*operand_2
