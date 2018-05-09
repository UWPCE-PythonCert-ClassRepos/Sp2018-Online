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

    # # TODO: write a test or tests for each of the behaviors defined for
    # #       Decider.decide
    #
    # def test_dummy(self):
    #     """
    #     Just some example syntax that you might use
    #     """
    #
    #     pump = Pump('127.0.0.1', 8000)
    #     pump.set_state = MagicMock(return_value=True)
    #
    #     self.fail("Remove this test.")

    def setUp(self):
        """Run each time before any test method is run."""
        self.pump = Pump('127.0.0.1', 8000)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

        self.decider = Decider(100, 0.05)

    def test_off_and_below_then_pump_in(self):
        """Test behavior 1.

        1. If the pump is off and the height is below the margin region,
        then the pump should be turned to PUMP_IN.
        """
        self.assertEqual(self.decider.decide(90, 0, self.actions),
                         self.pump.PUMP_IN
                         )

    def test_off_and_above_then_pump_out(self):
        """Test behavior 2.

        2. If the pump is off and the height is above the margin region, then
        the pump should be turned to PUMP_OUT.
        """
        self.assertEqual(self.decider.decide(110, 0, self.actions),
                         self.pump.PUMP_OUT
                         )

    def test_off_and_within_then_pump_off(self):
        """Test behavior 3.

        3. If the pump is off and the height is within the margin region or on
        the exact boundary of the margin region, then the pump shall remain at
        PUMP_OFF.
        """
        # pump off and height at the margin boundary then pump remains off
        self.assertEqual(self.decider.decide(105, 0, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump off and height at the margin boundary then pump remains off
        self.assertEqual(self.decider.decide(95, 0, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump off and height is withon margin then pump remains off
        self.assertEqual(self.decider.decide(101, 0, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump off and height is withon margin then pump remains off
        self.assertEqual(self.decider.decide(100, 0, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump off and height is withon margin then pump remains off
        self.assertEqual(self.decider.decide(99, 0, self.actions),
                         self.pump.PUMP_OFF
                         )

    def test_in_and_above_then_pump_off_else_in(self):
        """Test behavior 4.

        4. If the pump is performing PUMP_IN and the height is above the
        target height, then the pump shall be turned to PUMP_OFF, otherwise
        the pump shall remain at PUMP_IN.
        """
        # pump in and height above target then pump off
        self.assertEqual(self.decider.decide(101, 1, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump in and height below  target then pump in
        self.assertEqual(self.decider.decide(99, 1, self.actions),
                         self.pump.PUMP_IN
                         )
        # pump in and height at target then pump in
        self.assertEqual(self.decider.decide(100, 1, self.actions),
                         self.pump.PUMP_IN
                         )

    def test_out_and_below_then_pump_off_else_out(self):
        """Test behavior 5.

        5. If the pump is performing PUMP_OUT and the height is below
        the target height, then the pump shall be turned to PUMP_OFF,
        otherwise, the pump shall remain at PUMP_OUT.
        """
        # pump out and height is below then pump off
        self.assertEqual(self.decider.decide(99, -1, self.actions),
                         self.pump.PUMP_OFF
                         )
        # pump out but height is at target then pump remains out
        self.assertEqual(self.decider.decide(100, -1, self.actions),
                         self.pump.PUMP_OUT
                         )
        # pump out but height is above target then pump remains out
        self.assertEqual(self.decider.decide(110, -1, self.actions),
                         self.pump.PUMP_OUT
                         )

class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    pass
