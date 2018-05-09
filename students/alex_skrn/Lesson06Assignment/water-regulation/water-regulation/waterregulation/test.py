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

    def test_decider_init(self):
        """Test that decider gets intantiated with expected params."""
        self.assertIsInstance(self.decider, Decider)
        self.assertEqual(self.decider.target_height, 100)
        self.assertEqual(self.decider.margin, 0.05)

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
    """Unit tests for the Controller class."""

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    # pass
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

    def test_controller_init(self):
        """Test that controller gets intantiated with expected params."""
        self.assertIsInstance(self.controller, Controller)
        self.assertIsInstance(self.controller.sensor, Sensor)
        self.assertIsInstance(self.controller.pump, Pump)
        self.assertIsInstance(self.controller.decider, Decider)
        self.assertEqual(self.controller.actions, self.actions)

    def test_controller_tick_true_when_pump_acknowledged_state(self):
        """Test that tick returns True when pump acknowledged a new state."""
        # Provided that all external objects within tick work as expected
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        # And provided that the pump acknowledged a new state
        self.pump.set_state = MagicMock(return_value=True)

        # Now tick must return True
        self.assertTrue(self.controller.tick())

    def test_controller_tick_false_when_pump_does_not_acknowledge_state(self):
        """Test that tick returns True when pump acknowledged a new state."""
        # Provided that all external objects within tick work as expected
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        # And provided that the pump failed to acknowledge a new state
        self.pump.set_state = MagicMock(return_value=False)

        # Now tick must return False
        self.assertFalse(self.controller.tick())

    def test_tick_calls_sensor_measure(self):
        """Test that all methods within tick are called with right args."""
        self.sensor.measure = MagicMock(return_value=90)
        self.pump.get_state = MagicMock(return_value=0)
        self.decider.decide = MagicMock(return_value=1)
        self.pump.set_state = MagicMock()

        self.controller.tick()
        self.sensor.measure.assert_called_with()
        self.pump.get_state.assert_called_with()
        self.decider.decide.assert_called_with(90, 0, self.actions)
        self.pump.set_state.assert_called_with(1)
