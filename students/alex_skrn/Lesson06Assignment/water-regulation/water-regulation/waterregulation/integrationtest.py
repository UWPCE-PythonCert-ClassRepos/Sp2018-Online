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
        """Run each time before any test method is run."""
        self.sensor = Sensor('http://127.0.0.1', '8000')
        self.pump = Pump('http://127.0.0.1', '8000')
        self.decider = Decider(100, 0.05)

        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

    def test_module_with_decider_behavior_one_tick_true(self):
        """Test that the module acts as expected for the given scenario."""
        # With mocked sensor and pump methods
        # Start with initial water height 90, i.e. 10 units below target
        self.sensor.measure = MagicMock(return_value=90)
        # And initial pump state OFF
        self.pump.get_state = MagicMock(return_value=0)
        # And the pump acknowledges a new state
        self.pump.set_state = MagicMock(return_value=True)

        #  So tick should returns true
        self.assertTrue(self.controller.tick())

    def test_module_with_decider_behavior_one_tick_true(self):
        """Test that the module acts as expected for decider behavior 1."""
        # With mocked sensor and pump methods
        # Start with initial water height 90, i.e. 10 units below target
        self.sensor.measure = MagicMock(return_value=90)
        # And initial pump state OFF
        self.pump.get_state = MagicMock(return_value=0)

        # But the pump rejects a new state
        self.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
