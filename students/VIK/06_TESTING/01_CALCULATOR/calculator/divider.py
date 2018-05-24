"""
Module that defines a Divider operator class with Divider.calc to perform the calculation
"""

class Divider(object):
    """
    Class that used to feed the Calculator module __init__
    """
    @staticmethod
    def calc(operand_1, operand_2):
        """
        Method, divides 2 args. Throws a ZeroDivisionError for arg2 = 0
        :param operand_1: int or float
        :param operand_2: int or float
        :return: float
        """
        if operand_2 == 0:
            raise ZeroDivisionError("Divided by 0")
        return operand_1/operand_2
