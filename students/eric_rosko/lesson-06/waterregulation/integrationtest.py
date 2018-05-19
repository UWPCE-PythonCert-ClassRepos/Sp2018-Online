#!/usr/bin/env python3
"""
Module tests for the water-regulation module

pylint waterregulation

Usage: coverage run --source=waterregulation  -m unittest waterregulation/integrationtest.py waterregulation/test.py; coverage report

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

    # write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.
    def test_integration_set_pump_state(self):
        '''
        Test for a successful pump set state return value
        '''
        decider = Decider(5, 2)
        pump = Pump('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value=True)
        pump.get_state = MagicMock(return_value=Pump.PUMP_IN)

        sensor = Sensor('127.0.0.1', 8000)
        sensor.measure = MagicMock(return_value=3)

        controller = Controller(sensor, pump, decider)
        self.assertEqual(controller.tick(), True)


    def test_sanity(self):
        '''
        Test for a failed pump set state return value
        '''
        decider = Decider(5, 2)
        pump = Pump('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value=False)
        pump.get_state = MagicMock(return_value=Pump.PUMP_IN)

        sensor = Sensor('127.0.0.1', 8000)
        sensor.measure = MagicMock(return_value=3)

        controller = Controller(sensor, pump, decider)
        self.assertEqual(controller.tick(), False)
