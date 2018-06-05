"""
This module provides divider operator
"""
class Divider(object):
    """ divider class"""

    @staticmethod
    def calc(operand_1, operand_2):
        """
        :param operand_1: variable 1
        :param operand_2: variable 2
        :return: returns variable 1 divided by variable 2. If varaible 2 equals 0 returns error
        """
        try:
            return operand_1/operand_2
        except ZeroDivisionError as error_e:
            return error_e
