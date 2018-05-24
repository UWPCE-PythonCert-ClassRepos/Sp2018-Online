"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump.pump import Pump
from sensor.sensor import Sensor

from waterregulation.controller import Controller
from waterregulation.decider import Decider


class SensorTests(unittest.TestCase):
    """
    Unit tests for the Sensor class
    """
    def setUp(self):
        """
        setup for PumpTest class
        :return:
        """
        self.sensor = Sensor('127.1.1.3', 9000)

    def test_set_state(self):
        """
        test setting the state of pump
        :return:
        """
        self.sensor.measure = MagicMock(return_value=True)
        self.assertEqual(self.sensor.measure(), True)


class PumpTests(unittest.TestCase):
    """
    Unit tests for the Pump class
    """
    def setUp(self):
        """
        setup for PumpTest class
        :return:
        """
        self.pump = Pump('127.0.0.1', 8000)

    def test_set_state(self):
        """
        test setting the state of pump
        :return:
        """

        self.pump.set_state = MagicMock(return_value=True)
        self.pump.set_state('PUMP_IN')
        self.pump.set_state.assert_called_with('PUMP_IN')

    def test_get_state(self):
        """
        test calling get state of pump
        :return:
        """
        self.pump.get_state = MagicMock(return_value=1)
        self.assertEqual(self.pump.get_state(), 1)


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def setUp(self):
        """
        setup
        :return:
        """
        self.decider = Decider(100, 0.05)

    def test_decide(self):
        """
        test decide method from Decider class
        """

        pump = Pump('127.0.0.1', 8000)

        actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        self.assertEqual(self.decider.decide(110, 'PUMP_OFF', actions), 1)
        self.assertEqual(self.decider.decide(60, 'PUMP_OFF', actions), -1)
        self.assertEqual(self.decider.decide(105, 'PUMP_OFF', actions), 0)
        self.assertEqual(self.decider.decide(120, 'PUMP_IN', actions), 0)
        self.assertEqual(self.decider.decide(90, 'PUMP_OUT', actions), 0)
        self.assertEqual(self.decider.decide(115, 'PUMP_OUT', actions), -1)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def setUp(self):
        """
        setup
        :return:
        """
        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('127.1.1.3', 9000)
        self.decider = Decider(100, 0.05)

        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_tick(self):
        """
        test tick of Controller class
        :return:
        """
        self.sensor.measure = MagicMock(return_value=110)
        self.pump.get_state = MagicMock(return_value='PUMP_OFF')
        self.controller.tick = MagicMock(return_value='PUMP_IN')
        self.controller.tick()
        self.assertEqual(self.controller.tick(), 'PUMP_IN')


if __name__ == '__main__':
    unittest.main()
