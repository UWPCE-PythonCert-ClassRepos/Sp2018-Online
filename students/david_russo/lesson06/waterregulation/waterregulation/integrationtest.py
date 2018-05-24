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
        """
        setUp method for running each test.
        """
        self.sensor = Sensor('127.0.0.1', 8000)
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(5, 0.1)

        self.actions = {
            'PUMP_IN': self.pump.PUMP_IN,
            'PUMP_OUT': self.pump.PUMP_OUT,
            'PUMP_OFF': self.pump.PUMP_OFF,
        }

        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_determine_next_state(self):
        """
        Test that tick returns true when given mocked data to
        yield a response of True.
        """

        self.sensor.measure = MagicMock(return_value=4)
        self.pump.get_state = MagicMock(return_value=0)
        self.decider.decide = MagicMock(return_value=self.actions['PUMP_IN'])
        self.pump.set_state = MagicMock(return_value=True)

        self.assertEqual(self.controller.tick(), True)
