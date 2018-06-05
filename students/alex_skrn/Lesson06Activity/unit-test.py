#!/usr/bin/env python3
"""This module provides unit tests for the calculator."""

from unittest import TestCase
from unittest.mock import MagicMock

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands


class AdderTests(TestCase):
    """Provide a class for unit-testing the addition operator."""

    def test_adding(self):
        """For a range of numbers, expected value must equal actual value."""
        adder = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTests(TestCase):
    """Provide a class for unit-testing the subtraction operator."""

    def test_subtracting(self):
        """For a range of numbers, expected value must equal actual value."""
        subtracter = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))


class MultiplierTests(TestCase):
    """Provide a class for unit-testing the multiplication operator."""

    def test_multiplying(self):
        """For a range of numbers, expected value must equal actual value."""
        multiplier = Multiplier()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiplier.calc(i, j))


class DividerTests(TestCase):
    """Provide a class for unit-testing the division operator."""

    def test_dividing(self):
        """For a range of numbers, expected value must equal actual value."""
        divider = Divider()

        for i in range(-10, 10):
            for j in range(-10, 10):
                try:
                    self.assertEqual(i / j, divider.calc(i, j))
                except ZeroDivisionError:
                    pass


class CalculatorTests(TestCase):
    """Provide a class for unit-testing the calculator."""

    def setUp(self):
        """Provide a method to run each time before any test method is run."""
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

        self.calculator = Calculator(self.adder,
                                     self.subtracter,
                                     self.multiplier,
                                     self.divider
                                     )

    def test_insufficient_operands(self):
        """Raise the expected exception if not enough operands on stack."""
        self.calculator.enter_number(0)

        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        """Test that the method call is called with the expected arguments."""
        # This replaces the calc method with mock
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        # Calculator is to call its adder's call method with operands 1 and 2
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        """Test that the method call is called with the expected arguments."""
        # This replaces the calc method with mock
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)

    def test_multiplier_call(self):
        """Test that the method call is called with the expected arguments."""
        # This replaces the calc method with mock
        self.multiplier.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.multiply()

        self.multiplier.calc.assert_called_with(1, 2)

    def test_divider_call(self):
        """Test that the method call is called with the expected arguments."""
        # This replaces the calc method with mock
        self.divider.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.divide()

        self.divider.calc.assert_called_with(1, 2)
