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

    # TODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.

    def setUp(self):
        self.decider = Decider(205, .06)
        self.sensor = Sensor('127.0.0.1', 9011)
        self.pump = Pump('127.0.0.1', 9010)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_integration(self):
        """
        Integration test for controller and decider modules
        """
        self.sensor.measure = MagicMock(return_value=50)
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_IN)
        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())

        self.sensor.measure = MagicMock(return_value=100)
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_IN)
        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())

        self.sensor.measure = MagicMock(return_value=50)
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_IN)
        self.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
