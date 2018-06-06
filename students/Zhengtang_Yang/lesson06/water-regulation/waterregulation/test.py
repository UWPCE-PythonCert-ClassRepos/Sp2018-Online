"""
Unit tests for the water-regulation module
coverage run --include=waterregulation/controller.py,waterregulation/decider.py 
-m unittest waterregulation/test.py
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

    def setUp(self):
        """
        Just some example syntax that you might use
        """
        self.decider = Decider(100,0.05)
        self.actions = {
            'PUMP_IN': 1,
            'PUMP_OUT': -1,
            'PUMP_OFF': 0,
        }


    def test_decide_off(self):
        a = self.decider.decide(80, self.actions['PUMP_OFF'],self.actions)
        b = self.actions['PUMP_IN']
        self.assertEqual(a,b)

        a = self.decider.decide(120, self.actions['PUMP_OFF'],self.actions)
        b = self.actions['PUMP_OUT']
        self.assertEqual(a,b)
        
        a = self.decider.decide(100, self.actions['PUMP_OFF'],self.actions)
        b = self.actions['PUMP_OFF']
        self.assertEqual(a,b)

    def test_decide_in(self):
        a = self.decider.decide(120, self.actions['PUMP_IN'],self.actions)
        b = self.actions['PUMP_OFF']
        self.assertEqual(a,b)

        a = self.decider.decide(80, self.actions['PUMP_IN'],self.actions)
        b = self.actions['PUMP_IN']
        self.assertEqual(a,b)

    def test_decide_out(self):
        a = self.decider.decide(80, self.actions['PUMP_OUT'],self.actions)
        b = self.actions['PUMP_OFF']
        self.assertEqual(a,b)

        a = self.decider.decide(120, self.actions['PUMP_OUT'],self.actions)
        b = self.actions['PUMP_OUT']
        self.assertEqual(a,b)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    def setUp(self):
        """
        Just some example syntax that you might use
        """

        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('0.0.0.1', 1)
        self.decider = Decider(100,0.05)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_tick(self):
        self.sensor.measure = MagicMock(return_value=80)
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.pump.set_state = MagicMock(return_value=True)
        self.assertTrue(self.controller.tick())

        self.pump.set_state = MagicMock(return_value=False)
        self.assertFalse(self.controller.tick())
        

