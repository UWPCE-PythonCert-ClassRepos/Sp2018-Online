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

    def setUp(self):
        """
        setUp method for running each test. Set up with default address
        and port.
        """

        self.pump = Pump('127.0.0.1', 8000)
        self.actions = {
            'PUMP_IN': self.pump.PUMP_IN,
            'PUMP_OUT': self.pump.PUMP_OUT,
            'PUMP_OFF': self.pump.PUMP_OFF,
        }
        self.decider = Decider(5, 0.1)

    def test_pump_off_below_margin(self):
        """
        Behavior 1 from the decider class: If the pump is off and the water
        is below the margin, it should pump water in. Since the lower margin
        is 4.5, and if the current level is 4, it should pump in.
        """
        decider_1 = self.decider.decide(4, self.pump.PUMP_OFF, self.actions)

        self.assertEqual(decider_1, self.pump.PUMP_IN)

    def test_pump_off_above_margin(self):
        """
        Behavior 2 from the decider class: If the pump is off and the water
        is above the margin, it should pump water out. Since the upper margin
        is 5.5, and if the current level is 6, it should pump out.
        """
        decider_2 = self.decider.decide(6, self.pump.PUMP_OFF, self.actions)

        self.assertEqual(decider_2, self.pump.PUMP_OUT)

    def test_pump_off_within_margin(self):
        """
        Behavior 3 from the decider class: If the pump is off and the water
        level is within the margins, it should remain off. Since the margins
        are 4.5 and 5.5, and if the current level is 5.1, the pump should
        stay off.
        """
        decider_3 = self.decider.decide(5.1, self.pump.PUMP_OFF, self.actions)

        self.assertEqual(decider_3, self.pump.PUMP_OFF)

    def test_pump_in_above_target(self):
        """
        Behavior 4a from the decider class: If the pump is pumping in and the
        water level is above the target, the pump should be turned off. Since
        the target is 5, and if the level is at 10, it should turn off.
        """
        decider_4a = self.decider.decide(10, self.pump.PUMP_IN, self.actions)

        self.assertEqual(decider_4a, self.pump.PUMP_OFF)

    def test_pump_in_below_target(self):
        """
        Behavior 4b from the decider class: If the pump is pumping in and the
        water level is below the target, the pump shall continue to pump in.
        Since the target is 5, and if the level is at 1, it should remain on.
        """
        decider_4b = self.decider.decide(1, self.pump.PUMP_IN, self.actions)

        self.assertEqual(decider_4b, self.pump.PUMP_IN)

    def test_pump_out_below_target(self):
        """
        Behavior 5a from the decider class. If the pump is pumping out and the
        water level is below the target, it shall turn off. Since the target is
        5 and if the water level is at 4.9, it should turn off.
        """
        decider_5a = self.decider.decide(4.9, self.pump.PUMP_OUT, self.actions)

        self.assertEqual(decider_5a, self.pump.PUMP_OFF)

    def test_pump_out_above_target(self):
        """
        Behavior 5b from the decider class. If the pump is pumping out and the
        water level is above the target, it shall continue to pump out. Since
        the target is 5 and if the water level is at 5.1, it should continue
        to pump out.
        """
        decider_5b = self.decider.decide(5.1, self.pump.PUMP_OUT, self.actions)

        self.assertEqual(decider_5b, self.pump.PUMP_OUT)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
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

    def test_determine_next_state_true(self):
        """
        Test that tick returns true when given mocked data to
        yield a response of True.
        """

        self.sensor.measure = MagicMock(return_value=4)
        self.pump.get_state = MagicMock(return_value=0)
        self.decider.decide = MagicMock(return_value=self.actions['PUMP_IN'])
        self.pump.set_state = MagicMock(return_value=True)

        self.assertEqual(self.controller.tick(), True)

    def test_determine_next_state_false(self):
        """
        Test that tick returns true when given mocked data to
        yield a response of True.
        """

        self.sensor.measure = MagicMock(return_value=4)
        self.pump.get_state = MagicMock(return_value=-1)
        self.decider.decide = MagicMock(return_value=self.actions['PUMP_OFF'])
        self.pump.set_state = MagicMock(return_value=False)

        self.assertEqual(self.controller.tick(), False)
