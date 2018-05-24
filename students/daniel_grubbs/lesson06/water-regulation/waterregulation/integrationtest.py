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

    #       using a MOCKED sensor and pump.

    def setUp(self):
        """Method for setting up our criteria"""
        # Define the sensor, pump and decider to use with a Controller
        self.sensor = Sensor('http://127.0.0.1', 8000)  # IP Address and Port
        self.pump = Pump('http://127.0.0.1', 8000)  # IP Address and Port
        self.decider = Decider(50, 0.025)  # requires target_height and margin

        # Controller requires sensor, pump, decider (in order)
        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {
            'PUMP_IN': self.pump.PUMP_IN,
            'PUMP_OUT': self.pump.PUMP_OUT,
            'PUMP_OFF': self.pump.PUMP_OFF,
        }

    def test_module_true(self):
        """Test for True with Controller tick method."""
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())

    def test_module_tick_false(self):
        """Test for False with Controller tick method."""
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
