"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    def setUp(self):
        self.pump = Pump('127.0.0.1', 8010)
        self.decider = Decider(100, 0.05)
        self.sensor = Sensor('127.0.0.1', '8011')
        self.controller = Controller(self.sensor, self.pump, self.decider)
        self.actions = self.controller.actions

    def test_integration(self):
        """ Integration tests for both controller and decider """
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.sensor.measure = MagicMock(return_value=40)
        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick(), Pump.PUMP_IN)

        self.pump.get_state = MagicMock(return_value=Pump.PUMP_IN)
        self.sensor.measure = MagicMock(return_value=110)
        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick(), Pump.PUMP_OFF)
