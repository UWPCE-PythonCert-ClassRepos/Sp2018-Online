from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands

if __name__ == '__main__':
    add = Adder()
    sub = Subtracter()
    multi = Multiplier()
    div = Divider()
    test_1 = Calculator(add,sub,multi,div)
    test_1.enter_number(1)
    test_1.enter_number(2)

    temp_num = test_1.add()
    print (temp_num)

