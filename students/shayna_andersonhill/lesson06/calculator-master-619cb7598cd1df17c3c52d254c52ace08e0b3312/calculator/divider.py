class Divider(object):

    @staticmethod
    def calc(operand_1, operand_2):
        try:
            return operand_1/operand_2
        except ZeroDivisionError:
            print("You can't divide by zero!")
