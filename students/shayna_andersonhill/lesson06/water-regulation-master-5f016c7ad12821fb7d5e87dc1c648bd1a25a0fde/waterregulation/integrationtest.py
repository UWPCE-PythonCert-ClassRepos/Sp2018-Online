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
        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('127.0.0.1', 8000)
        self.decider = Decider(target_height = 100, margin = 0.05)
        self.controller = Controller(self.sensor, self.pump,
                self.decider)
        self.actions = self.controller.actions

    def test_module(self):
        self.sensor.measure = MagicMock(return_value = 90)
        self.pump.get_state = MagicMock(return_value =
        'PUMP_OFF')
        self.pump.set_state = MagicMock(return_value = True)

        self.assertFalse(self.controller.tick())

   
    

