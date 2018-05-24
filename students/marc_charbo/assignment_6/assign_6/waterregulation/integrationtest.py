"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump.pump import Pump
from sensor.sensor import Sensor

from waterregulation.controller import Controller
from waterregulation.decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
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
        self.assertEqual(self.controller.tick(), 'PUMP_IN')


if __name__ == '__main__':
    unittest.main()
