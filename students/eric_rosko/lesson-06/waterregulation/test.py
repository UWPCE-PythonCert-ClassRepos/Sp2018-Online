#!/usr/bin/env python3

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
        '''
        setup
        '''
        self.decider = Decider(5, 2)
        self.pump = Pump('127.0.0.1', 8000)
        self.sensor = Sensor('127.0.0.1', 8000)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_one(self):
        '''
        #   1. If the pump is off and the height is below the margin region,
        then the
        #      pump should be turned to PUMP_IN.
        '''
        self.assertEqual(self.decider.decide(3,
                                             Pump.PUMP_OFF,
                                             self.controller.actions),
                         Pump.PUMP_OFF)

    def test_two(self):
        '''
        #   2. If the pump is off and the height is above the margin region,
        then the
        #      pump should be turned to PUMP_OUT.
        '''
        self.assertEqual(self.decider.decide(8,
                                             Pump.PUMP_OFF,
                                             self.controller.actions),
                         Pump.PUMP_OUT)

    def test_three(self):
        '''
        #   3. If the pump is off and the height is within the margin region
         or on
        #      the exact boundary of the margin region, then the pump shall
        remain at
        #      PUMP_OFF.
        '''
        self.assertEqual(self.decider.decide(3,
                                             Pump.PUMP_OFF,
                                             self.controller.actions),
                         Pump.PUMP_OFF)

    def test_three_high_level(self):
        '''
        #   3. If the pump is off and the height is within the margin region
         or on
        #      the exact boundary of the margin region, then the pump shall
        remain at
        #      PUMP_OFF.
        '''
        self.assertEqual(self.decider.decide(7,
                                             Pump.PUMP_OFF,
                                             self.controller.actions),
                         Pump.PUMP_OFF)

    def test_four(self):
        '''
        #   4. If the pump is performing PUMP_IN and the height is above the
         target
        #      height, then the pump shall be turned to PUMP_OFF, otherwise
         the pump
        #      shall remain at PUMP_IN.
        '''
        self.assertEqual(self.decider.decide(6,
                                             Pump.PUMP_IN,
                                             self.controller.actions),
                         Pump.PUMP_OFF)

    def test_four_no_change(self):
        '''
        #   4. If the pump is performing PUMP_IN and the height is above the
         target
        #      height, then the pump shall be turned to PUMP_OFF, otherwise
        the pump
        #      shall remain at PUMP_IN.
        '''
        self.assertEqual(self.decider.decide(4,
                                             Pump.PUMP_IN,
                                             self.controller.actions),
                         Pump.PUMP_IN)

    def test_five(self):
        '''
        #   5. If the pump is performing PUMP_OUT and the height is below the
         target
        #      height, then the pump shall be turned to PUMP_OFF, otherwise,
        the pump
        #      shall remain at PUMP_OUT.
        '''
        self.assertEqual(self.decider.decide(3,
                                             Pump.PUMP_OUT,
                                             self.controller.actions),
                         Pump.PUMP_OFF)

    def test_five_with_value_at_target(self):
        '''
        another test
        '''
        self.assertEqual(self.decider.decide(5,
                                             Pump.PUMP_OUT,
                                             self.controller.actions),
                         Pump.PUMP_OUT)


class ControllerTests(unittest.TestCase):
    '''
    main unittest class for the Controller
    '''

    def test_integration(self):
        '''
        I can see how you could use mocks to provide data for classes that
        aren't
        actually implemented yet.  However, since both the set_state and

        get_state methods of pump are overridden the code doesn't seem to
         really
        test anything except that it doesn't crash.

        The important part, the decide method, is covered in the unit tests
        so I guess this mock method is as good as we can test until the
        pump and sensor are actually hooked up to live objects.

        I can see how the test can be converted to test real objects by just
        taking out the mock method assignments.
        '''
        decider = Decider(4, 3)
        pump = Pump('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value=False)
        pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)

        sensor = Sensor('127.0.0.1', 8000)
        sensor.measure = MagicMock(return_value=3)

        controller = Controller(sensor, pump, decider)
        self.assertEqual(controller.tick(), False)
