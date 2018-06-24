import unittest
from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator



class ModuleTests(unittest.TestCase):
    
    '''Integration test: In order to get it to pass, had to swap places of operand_1
    and operand_2 in divider and subrtractor module'''

    def test_module(self):

        '''Runs the actual integration test, going through all calculator calls
        and testing the end result'''
                
        calculator = Calculator(Adder(), Subtracter(), Multiplier(), Divider())
        calculator.enter_number(5)
        calculator.enter_number(2)
        calculator.multiply()
        calculator.enter_number(46)
        calculator.add()
        calculator.enter_number(8)
        calculator.divide()
        calculator.enter_number(1)
        result = calculator.subtract()
        assert result == 6
                
if __name__ == "__main__":
    my_module = ModuleTests()
    my_module.test_module()
