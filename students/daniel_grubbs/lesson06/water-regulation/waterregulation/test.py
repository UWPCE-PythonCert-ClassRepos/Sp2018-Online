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
    """Unit tests for the Decider class.

    Use the target_height as 50 and margin as 2.5% for testing.
    """

    # Decider.decide
    # Decider tests to perform: __init__, decide method with the
    # 5 behaviors defined.

    def setUp(self):
        """setUp() method is executed before test methods run for Decider."""
        # could also use localhost instead of 127.0.0.1
        self.pump = Pump('127.0.0.1', 8000)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

        self.decider = Decider(50, 0.025)

        # breakdown of using decider with the values 50 and 2.5%
        # Below - 48.75
        # Above - 51.25

        # Reference
        # PUMP_IN = 1
        # PUMP_OFF = 0
        # PUMP_OUT = -1

    def test_decider_init(self):
        """Test the constructor that it takes in the
        target_height and margin.
        """
        self.assertIsInstance(self.decider, Decider)
        self.assertEqual(self.decider.target_height, 50)
        self.assertEqual(self.decider.margin, 0.025)

    def test_decider_behavior_one(self):
        """Test behavior one.

        1. If the pump is off and the height is below the margin region,
        then the pump should be turned to PUMP_IN.
        """
        # Couple ways to test, using the numbers or using the format of
        # self.pump,PUMP_<state>
        # Playing around with for behaviour one.
        self.assertEqual(self.decider.decide(45, 0, self.actions),
                         1)

        self.assertEqual(self.decider.decide(45, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_IN)

    def test_decider_behaviour_two(self):
        """Test behavior two.

        2. If the pump is off and the height is above the margin region,
        then the pump should be turned to PUMP_OUT.
        """
        self.assertEqual(self.decider.decide(55, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OUT)

    def test_decider_behavior_three(self):
        """Test behavior three.

        3. If the pump is off and the height is within the margin region
        or on the exact boundary of the margin region, then the pump shall
        remain at PUMP_OFF.
        """

        self.assertEqual(self.decider.decide(51, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

        self.assertEqual(self.decider.decide(49.75, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

        self.assertEqual(self.decider.decide(50, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

        # Check the boundaries
        self.assertEqual(self.decider.decide(51.25, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

        self.assertEqual(self.decider.decide(48.75, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

    def test_decider_behavior_four(self):
        """Test behavior four.

        4. If the pump is performing PUMP_IN and the height is above
        the target height, then the pump shall be turned to PUMP_OFF,
        otherwise the pump shall remain at PUMP_IN.
        """
        self.assertEqual(self.decider.decide(51.25, self.pump.PUMP_IN,
                                             self.actions), self.pump.PUMP_OFF)
        self.assertEqual(self.decider.decide(49, self.pump.PUMP_IN,
                                             self.actions), self.pump.PUMP_IN)

    def test_decider_behavor_five(self):
        """Test last behavior.

        5. If the pump is performing PUMP_OUT and the height is below
        the target height, then the pump shall be turned to PUMP_OFF,
        otherwise, the pump shall remain at PUMP_OUT.
        """
        self.assertEqual(self.decider.decide(47, self.pump.PUMP_OUT,
                                             self.actions), self.pump.PUMP_OFF)

        self.assertEqual(self.decider.decide(55, self.pump.PUMP_OUT,
                                             self.actions), self.pump.PUMP_OUT)


class ControllerTests(unittest.TestCase):
    """Unit tests for the Controller class."""

    #       Controller.tick
    # Controller tests to perform: __init__, calling tick
    # with defined behaviours

    def setUp(self):
        """setUp() method is executed before test methods
        run for Controller."""
        self.sensor = Sensor('http://127.0.0.1', '8000')
        self.pump = Pump('http://127.0.0.1', '8000')
        self.decider = Decider(50, 0.025)

        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

    def test_controller_init(self):
        """Test the constructor for creating a new instance."""
        self.assertIsInstance(self.controller, Controller)
        self.assertIsInstance(self.controller.sensor, Sensor)
        self.assertIsInstance(self.controller.pump, Pump)
        self.assertIsInstance(self.controller.decider, Decider)
        self.assertEqual(self.controller.actions, self.actions)

    def test_state_of_tick_true(self):
        """Test for True if the pump has acknowledged its new state."""
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        self.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())

    def test_state_of_tick_false(self):
        """Test if the pump has not acknowledged its new
        state resulting in False."""
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        self.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
