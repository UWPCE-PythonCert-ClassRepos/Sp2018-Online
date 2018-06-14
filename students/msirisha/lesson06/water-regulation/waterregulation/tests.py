"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def setUp(self):
        """ setup """
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(100, 0.05)
        self.sensor = Sensor('127.0.0.1', '8001')
        self.controller = Controller(self.sensor, self.pump, self.decider)
        self.actions = self.controller.actions

    def test_decider(self):
        """ Decider tests """

        # Pump off and level is below margin region
        self.assertEqual(self.decider.decide(90, self.actions['PUMP_OFF'],
                                             self.actions), self.actions['PUMP_IN'])

        # Pump Off and height is above margin region
        self.assertEqual(self.decider.decide(110, self.actions['PUMP_OFF'],
                                             self.actions), self.actions['PUMP_OUT'])

        # Pump OFF, level within margin
        self.assertEqual(self.decider.decide(102, self.actions['PUMP_OFF'],
                                             self.actions), self.actions['PUMP_OFF'])

        # Pump OFF, level within margin
        self.assertEqual(self.decider.decide(98, self.actions['PUMP_OFF'],
                                             self.actions), self.actions['PUMP_OFF'])

        # Pump In, current height greater than target height
        self.assertEqual(self.decider.decide(150, self.actions['PUMP_IN'],
                                             self.actions), self.actions['PUMP_OFF'])

        # Pump In, current height less than target height
        self.assertEqual(self.decider.decide(80, self.actions['PUMP_IN'],
                                             self.actions), self.actions['PUMP_IN'])

        # Pump Out current height less than target height
        self.assertEqual(self.decider.decide(50, self.actions['PUMP_OUT'],
                                             self.actions), self.actions['PUMP_OFF'])

        # Pump Out current height greater than target height
        self.assertEqual(self.decider.decide(150, self.actions['PUMP_OUT'],
                                             self.actions), self.actions['PUMP_OUT'])

        # Test passing input bad
        self.assertIsNone(self.decider.decide(100, 100, self.actions))

        # Setup mocks
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.sensor.measure = MagicMock(return_value=40)
        self.decider.decide = MagicMock(return_value=1)

        result = self.decider.decide(self.sensor.measure(), self.pump.get_state(), self.actions)
        self.decider.decide.assert_called_with(40, Pump.PUMP_OFF, self.actions)
        self.assertEqual(result, 1)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def setUp(self):
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(100, 0.05)
        self.sensor = Sensor('127.0.0.1', '8001')
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_controller(self):
        """ Controller tests """
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.sensor.measure = MagicMock(return_value=40)
        self.decider.decide = MagicMock(return_value=1)

        self.pump.set_state = MagicMock(return_value=True)
        self.assertTrue(self.controller.tick())

        self.pump.set_state = MagicMock(return_value=False)
        self.assertFalse(self.controller.tick())
