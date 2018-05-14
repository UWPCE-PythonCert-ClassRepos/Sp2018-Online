"""
Module tests for the water-regulation module
"""

from unittest import TestCase
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class ModuleTests(TestCase):
    """
    Module tests for the water-regulation module
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

    def test_module_true(self):
        '''True state: Write an integration test that combines controller and decider,
        using a MOCKED sensor and pump.
        '''
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()

        self.pump.set_state = MagicMock(return_value=True)
        self.assertTrue(self.controller.tick())

    def test_module_false(self):
        '''False state: Write an integration test that combines controller and decider,
        using a MOCKED sensor and pump.
        '''
        self.sensor.measure = MagicMock()
        self.pump.get_state = MagicMock()

        self.pump.set_state = MagicMock(return_value=False)
        self.assertFalse(self.controller.tick())