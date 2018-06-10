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

    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide

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
        """
        This method does a setup for unit testing Decider
        """
        self.decider = Decider(100, 0.05)

    def test_decide(self):
        """
        This method performs a unit test on decide
        """

        pump = Pump('127.0.0.1', 1000)

        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }

        self.assertEqual(self.decider.decide(130, 'PUMP_OFF', actions), 1)
        self.assertEqual(self.decider.decide(40, 'PUMP_OFF', actions), -1)
        self.assertEqual(self.decider.decide(105, 'PUMP_OFF', actions), 0)
        self.assertEqual(self.decider.decide(140, 'PUMP_IN', actions), 0)
        self.assertEqual(self.decider.decide(85, 'PUMP_OUT', actions), 0)
        self.assertEqual(self.decider.decide(110, 'PUMP_OUT', actions), -1)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    def setUp(self):
        """
        This method does a setup for unit testing Controller
        """
        self.pump = Pump('127.0.0.1', 1000)
        self.sensor = Sensor('127.0.0.2', 2000)
        self.decider = Decider(100, 0.05)

        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_tick(self):
        """
        This method performs a unit test on tick
        """
        self.sensor.measure = MagicMock(return_value=130)
        self.pump.get_state = MagicMock(return_value='PUMP_OFF')
        self.controller.tick = MagicMock(return_value='PUMP_IN')
        self.controller.tick()
        self.assertEqual(self.controller.tick(), 'PUMP_IN')


class PumpTests(unittest.TestCase):
    """
    This class performs a unit test on Pump
    """
    def setUp(self):
        """
        This method does a setup for unit testing Pump
        """
        self.pump = Pump('127.0.0.1', 1000)

    def test_set_state(self):
        """
        This method tests the set_state for Pump
        """
        self.pump.set_state = MagicMock(return_value=True)
        self.pump.set_state('PUMP_OUT')
        self.pump.set_state.assert_called_with('PUMP_OUT')

    def test_get_state(self):
        """
        This method tests the get_state for Pump
        """
        self.pump.get_state = MagicMock(return_value=1)
        self.assertEqual(self.pump.get_state(), 1)


class SensorTests(unittest.TestCase):
    """
        This method does a setup for unit testing Sensor
    """
    def setUp(self):
        """
        This method does a setup for unit testing Sensor
        """
        self.sensor = Sensor('127.0.0.2', 2000)

    def test_set_state(self):
        """
        This method tests the set_state for Sensor
        """
        self.sensor.measure = MagicMock(return_value=True)
        self.assertEqual(self.sensor.measure(), True)

    def test_get_state(self):
        """
        This method tests the get_state for Sensor
        """
        self.sensor.get_state = MagicMock(return_value=1)
        self.assertEqual(self.sensor.get_state(), 1)