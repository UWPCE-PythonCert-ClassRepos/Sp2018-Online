"""
Module tests for the water-regulation module
"""

import sys
import unittest
from unittest.mock import MagicMock
from sensor import Sensor
from pump import Pump
from .controller import Controller
from .decider import Decider
sys.path.append('../pump')
sys.path.append('../sensor')


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    def test_integration(self):
        """
        Test full integration of controller and decider components.
        """
        pump = Pump('127.0.0.1', "8000")
        pump.get_state = MagicMock(return_value=1)
        pump.set_state = MagicMock(return_value=True)
        sensor = Sensor('127.0.0.1', "8080")
        sensor.measure = MagicMock(return_value=120)
        decider = Decider(100, 0.05)
        controller = Controller(sensor, pump, decider)
        controller_called = controller.tick()
        sensor.measure.assert_called()
        pump.get_state.assert_called()
        pump.set_state.assert_called_with(-1)
        self.assertEqual(controller_called, True)
