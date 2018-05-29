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
    def setUp(self):
        sensor = Sensor(address="0.0.0.0", port=514)
        pump = Pump(address="0.0.0.0", port=514)
        decider = Decider(target_height=100, margin=.10)
        self.controller = Controller(sensor=sensor, pump=pump, decider=decider)


    # doneTODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.
    def test_int_tick_arg_pass(self):
        """
        test tick
        :return:
        """
        # running down the list on Controller.tick()
        self.controller.sensor.measure = MagicMock(return_value=89)
        self.controller.pump.get_state = MagicMock(return_value=0)
        self.controller.pump.set_state = MagicMock(return_value=True)
        self.controller.decider.decide = MagicMock(return_value=None)

        self.controller.tick()

        self.controller.decider.decide.assert_called_with(current_height=89, current_action=0,
                                                          actions=self.controller.actions)
