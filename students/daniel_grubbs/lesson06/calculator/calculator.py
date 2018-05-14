from exceptions import InsufficientOperands


class Calculator(object):
    """Calculator class."""

    def __init__(self, adder, subtracter, multiplier, divider):
        """Constructor for class."""
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """Enter a number."""
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """Calc."""
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """Addition."""
        return self._do_calc(self.adder)

    def subtract(self):
        """Subtraction."""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """Multiplication."""
        return self._do_calc(self.multiplier)

    def divide(self):
        """Division."""
        return self._do_calc(self.divider)
