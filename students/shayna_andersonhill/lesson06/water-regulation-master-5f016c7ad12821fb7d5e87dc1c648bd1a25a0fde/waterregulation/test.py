"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

import logging

from pump import Pump
from sensor import Sensor

from waterregulation.controller import Controller
from waterregulation.decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """
    
    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide

    def setUp(self):
        """
        Create instance for testing
        """
        self.decider = Decider(100, 0.05)
        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('127.0.0.1', 8000)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_init(self):
        """
        Test decider instance
        """
        self.decider.target_height == 100
        self.decider.margin == 0.05

    def test_1(self):
        """
        Test - If the pump is off and the height 
        is below the margin region, 
        then the pump should be turned to PUMP_IN
        """
        decision_instance = self.decider.decide(current_height = 80,
                current_action=self.controller.actions['PUMP_OFF'],
                actions=self.controller.actions)

        self.assertTrue(decision_instance ==
                self.controller.actions['PUMP_IN'])

    def test_2(self):
        """
        Test - If the pump is off and the height 
        is above the margin region, then the
             pump should be turned to PUMP_OUT.        
        """
        decision_instance = self.decider.decide(current_height = 110,
                current_action=self.controller.actions['PUMP_OFF'],
                actions=self.controller.actions)

        self.assertTrue(decision_instance ==
                self.controller.actions['PUMP_OUT'])

    def test_3(self):
        """
        Test - If the pump is off and the height is
        within the margin region or on the exact
        boundary of the margin region, then the 
        pump shall remain at PUMP_OFF.       
        """
        decision_instance = self.decider.decide(current_height = 100,
                current_action=self.controller.actions['PUMP_OFF'],
                actions=self.controller.actions)

        self.assertTrue(decision_instance ==
                self.controller.actions['PUMP_OFF'])

    def test_4(self):
        """
        Test - If the pump is performing PUMP_IN and 
        the height is above the target height, 
        then the pump shall be turned to PUMP_OFF,
        otherwise the pump shall remain at PUMP_IN.     
        """
        decision_instance = self.decider.decide(current_height = 120,
                current_action=self.controller.actions['PUMP_IN'],
                actions=self.controller.actions)

        self.assertTrue(decision_instance ==
                self.controller.actions['PUMP_OFF'])

    def test_5(self):
        """
        Test - If the pump is performing PUMP_OUT and 
        the height is below the target height, 
        then the pump shall be turned to PUMP_OFF, 
        otherwise, the pump shall remain at PUMP_OUT.      
        """
        decision_instance = self.decider.decide(current_height = 80,
                current_action=self.controller.actions['PUMP_OUT'],
                actions=self.controller.actions)
        self.assertTrue(decision_instance ==
                self.controller.actions['PUMP_OFF'])


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def setUp(self):
        self.decider = Decider(100, 0.05)
        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('127.0.0.1', 8000)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_tick(self):
        """
        Test tick method
        """
        self.controller.sensor.measure = MagicMock(return_value=80)
        self.controller.pump.get_state = MagicMock(return_value=0)
        self.controller.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())
