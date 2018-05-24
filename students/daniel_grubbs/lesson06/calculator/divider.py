class Divider(object):

    @staticmethod
    def calc(operand_1, operand_2):
        # Fixed issue with the unittest not passing
        return int(operand_1 // operand_2)