"""
Unit tests for the water-regulation module
"""

from unittest import TestCase
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(TestCase):
    """
    Unit tests for the Decider class
    Write a test or tests for each of the behaviors defined for
    Decider.decide
    """
    def setUp(self):
        """
        Run each time before any test method
        """
        self.decider = Decider(100, 0.05)
        self.pump = Pump('127.0.0.1', 8000)
        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

    def test_my_decider(self):
        '''
        Test the instance
        '''
        self.assertIsInstance(self.decider, Decider)
        self.assertEqual(self.decider.target_height, 100)
        self.assertEqual(self.decider.margin, 0.05)

    def test_decider_one(self):
        '''Case 1. If the pump is off and the height is below the
        margin region, then the pump should be turned to PUMP_IN

        Parameters: (current_height, current_action, actions)
        Return: return_action
        '''
        self.assertEqual(self.decider.decide(90, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_IN)

    def test_decider_two(self):
        '''Case 2. If the pump is off and the height is above the
        margin region, then the pump should be turned to PUMP_OUT
        '''
        self.assertEqual(self.decider.decide(110, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OUT)

    def test_decider_three(self):
        '''Case 3. If the pump is off and the height is within the
        margin region or on the exact boundary of the margin region,
        then the pump shall remain at PUMP_OFF.
        '''
        self.assertEqual(self.decider.decide(102, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)
        self.assertEqual(self.decider.decide(105, self.pump.PUMP_OFF,
                                             self.actions), self.pump.PUMP_OFF)

    def test_decider_four(self):
        '''Case 4. If the pump is performing PUMP_IN and the height
        is above the target height, then the pump shall be turned to
        PUMP_OFF, otherwise the pump shall remain at PUMP_IN.
        '''
        self.assertEqual(self.decider.decide(105, self.pump.PUMP_IN,
                                             self.actions), self.pump.PUMP_OFF)
        self.assertEqual(self.decider.decide(99, self.pump.PUMP_IN,
                                             self.actions), self.pump.PUMP_IN)

    def test_decider_five(self):
        '''Case 5. If the pump is performing PUMP_OUT and the height
        is below the target height, then the pump shall be turned to
        PUMP_OFF, otherwise, the pump shall remain at PUMP_OUT.
        '''
        self.assertEqual(self.decider.decide(99, self.pump.PUMP_OUT,
                                             self.actions), self.pump.PUMP_OFF)
        self.assertEqual(self.decider.decide(101, self.pump.PUMP_OUT,
                                             self.actions), self.pump.PUMP_OUT)


class ControllerTests(TestCase):
    """
    Unit tests for the Controller class
    Write a test or tests for each of the behaviors defined for
    Controller.tick
    """

    def setUp(self):
        """
        Run each time before any test method
        """
        self.sensor = Sensor('http://127.0.0.1', '8000')
        self.pump = Pump('http://127.0.0.1', '8000')
        self.decider = Decider(100, 0.05)
        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {'PUMP_IN': self.pump.PUMP_IN,
                        'PUMP_OUT': self.pump.PUMP_OUT,
                        'PUMP_OFF': self.pump.PUMP_OFF,
                        }

    def test_my_controller(self):
        '''
        Test the instance
        '''
        self.assertIsInstance(self.controller, Controller)
        self.assertIsInstance(self.controller.sensor, Sensor)
        self.assertIsInstance(self.controller.pump, Pump)
        self.assertIsInstance(self.controller.decider, Decider)
        self.assertEqual(self.controller.actions, self.actions)

    def test_tick_state_true(self):
        '''True tick state given: sensor.measure, pump.get_state, and
        decider.decide(cur_height, cur_state, self.actions)
        Return true based on pump.set_state(next_state)
        '''
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        self.pump.set_state = MagicMock(return_value=True)
        self.assertTrue(self.controller.tick())

    def test_tick_state_false(self):
        '''False tick state given: sensor.measure, pump.get_state, and
        decider.decide(cur_height, cur_state, self.actions)
        Return false based on pump.set_state(next_state)
        '''
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()
        self.decider.decide = MagicMock()

        self.pump.set_state = MagicMock(return_value=False)
        self.assertFalse(self.controller.tick())
