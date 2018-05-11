"""Module tests for the water-regulation module."""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class ModuleTests(unittest.TestCase):
    """Module tests for the water-regulation module."""

    # TODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.
    def setUp(self):
        """Run each time before any test method is run."""
        self.sensor = Sensor('http://127.0.0.1', '8000')
        self.pump = Pump('http://127.0.0.1', '8000')
        self.decider = Decider(100, 0.05)

        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

    def test_module_true(self):
        """Test the module by calling its main method -- tick."""
        # With mocked sensor and pump methods but not decider.decide method
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.pump.set_state = MagicMock(return_value=True)

        # So tick should returns true
        self.assertTrue(self.controller.tick())

    def test_module_false(self):
        """Test the module by calling its main method -- tick."""
        # With mocked sensor and pump methods
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        # But the pump rejects a new state
        self.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
