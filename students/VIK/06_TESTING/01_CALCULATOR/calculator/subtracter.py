"""
Module that defines a Subtracter operator class with Subtracter.calc to perform the calculation
"""


class Subtracter(object):
    """
    Class that used to feed the Calculator module __init__
    """
    @staticmethod
    def calc(operand_1, operand_2):
        """
        Method, subtracts 2 args
        :param operand_1: int or float
        :param operand_2: int or float
        :return: float
        """
        return operand_1 - operand_2
