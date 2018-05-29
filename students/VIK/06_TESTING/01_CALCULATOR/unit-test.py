#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import MagicMock

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands

class AdderTests(TestCase):

    def test_adding(self):
        adder = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTests(TestCase):

    def test_subtracting(self):
        subtracter = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))

class MultiplierTests(TestCase):

    def test_multiplier(self):
        multilper = Multiplier()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multilper.calc(i, j))


class DividerTests(TestCase):

    def test_divider(self):
        divider = Divider()

        for i in range(-10, 10):
            for j in range(-10, 10):
                if j == 0:
                    with self.assertRaises(ZeroDivisionError):
                        divider.calc(i, j)
                else:
                    self.assertEqual(i / j, divider.calc(i, j))


class CalculatorTests(TestCase):

    def setUp(self):
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

        self.calculator = Calculator(self.adder, self.subtracter, self.multiplier, self.divider)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)

        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)

    def test_multiplier_call(self):
        """
        Uses MagicMock to mock-up a call to self.multiplier.calc
        Notes:  self.multiplier is a direct call to the multiplier module
                self.calculator.multiplier is a production call to the same multiplier module

        :return: none
        """
        self.multiplier.calc = MagicMock(return_value=0)
        "MagicMock intercept all calls to self.multiplier.calc and does not actually let the call execute"

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.multiply()
        """"
        the production call of Multiplier is made through 
        1) calculator.multiply() that calls
        2) calculator._do_calc then in turn calls 
        3) calculator.multiply (the calculator instance attribute) that finally calls the 
        4) multiplier module Multiplier.calc which is intercepted by MagicMock
        """

        self.multiplier.calc.assert_called_with(1, 2)
        """
        the previous code: self.calculator.multiply() was intercepted by MagicMock with the passed in args 1 and 2
        now we can .assert_called_with() on the intercepted code to check that the agrs intended did in-fact make it 
        through the calculator.multiply() to the desired code call of Multiplier.calc
        """


    def test_divider_call(self):
        self.divider.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.divide()

        self.divider.calc.assert_called_with(1, 2)
