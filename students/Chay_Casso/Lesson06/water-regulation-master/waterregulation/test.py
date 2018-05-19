"""
Unit tests for the water-regulation module
"""

import sys
import unittest
from unittest.mock import MagicMock

sys.path.append('../pump')
sys.path.append('../sensor')

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def test_off_too_low(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(110, "PUMP_OFF", actions)
        self.assertEqual(actions["PUMP_OUT"], result)

    def test_off_too_high(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(90, "PUMP_OFF", actions)
        self.assertEqual(actions["PUMP_IN"], result)

    def test_off_just_right(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(100, "PUMP_OFF", actions)
        self.assertEqual(actions["PUMP_OFF"], result)

    def test_in_too_high(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(101, "PUMP_IN", actions)
        self.assertEqual(actions["PUMP_OFF"], result)

    def test_in_not_enough(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(96, "PUMP_IN", actions)
        self.assertEqual(actions["PUMP_IN"], result)

    def test_out_too_much(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(101, "PUMP_OUT", actions)
        self.assertEqual(actions["PUMP_OUT"], result)

    def test_out_not_enough(self):
        decider = Decider(100, 0.05)
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        result = decider.decide(99, "PUMP_OUT", actions)
        self.assertEqual(actions["PUMP_OFF"], result)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def test_controller(self):
        pump = Pump('127.0.0.1', "8000")
        pump.get_state = MagicMock(return_value=1)
        pump.set_state = MagicMock(return_value=True)
        sensor = Sensor('127.0.0.1', "8080")
        sensor.measure = MagicMock(return_value=120)
        decider = Decider(100, 0.05)
        decider.decide = MagicMock(return_value=1)
        controller = Controller(sensor, pump, decider)
        controller_called = controller.tick()
        sensor.measure.assert_called()
        pump.get_state.assert_called()
        decider.decide.assert_called_with(120,1,{
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        })
        self.assertEqual(controller_called, True)



