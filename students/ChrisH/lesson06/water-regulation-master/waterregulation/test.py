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

    # DONE: write a test or tests for each of the behaviors defined for
    #       Decider.decide

    def setUp(self):
        self.decider = Decider(100, .05)
        self.sensor = Sensor('127.0.0.1', 8001)
        self.pump = Pump('127.0.0.1', 8000)
        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.actions = {'PUMP_IN': Pump.PUMP_IN,
                   'PUMP_OFF': Pump.PUMP_OFF,
                   'PUMP_OUT': Pump.PUMP_OUT}

    def test_decider(self):
        """
        Test Decider module logic
        """

        # Pump OFF, level low
        self.assertEqual(self.decider.decide(50, self.actions['PUMP_OFF'], self.actions), self.actions['PUMP_IN'])
        # Pump OFF, level high
        self.assertEqual(self.decider.decide(150, self.actions['PUMP_OFF'], self.actions), self.actions['PUMP_OUT'])
        # Pump OFF, level within margin
        self.assertEqual(self.decider.decide(100, self.actions['PUMP_OFF'], self.actions), self.actions['PUMP_OFF'])
        self.assertEqual(self.decider.decide(102, self.actions['PUMP_OFF'], self.actions), self.actions['PUMP_OFF'])
        self.assertEqual(self.decider.decide(98, self.actions['PUMP_OFF'], self.actions), self.actions['PUMP_OFF'])

        # Pump IN, level above target
        self.assertEqual(self.decider.decide(150, self.actions['PUMP_IN'], self.actions), self.actions['PUMP_OFF'])
        # Pump IN, level below target
        self.assertEqual(self.decider.decide(50, self.actions['PUMP_IN'], self.actions), self.actions['PUMP_IN'])

        # Pump OUT, level below target
        self.assertEqual(self.decider.decide(50, self.actions['PUMP_OUT'], self.actions), self.actions['PUMP_OFF'])
        # Pump OUT, level above target
        self.assertEqual(self.decider.decide(150, self.actions['PUMP_OUT'], self.actions), self.actions['PUMP_OUT'])

        # Test bad input to decider actions
        self.assertIsNone(self.decider.decide(100, 100, self.actions))

        # MOCKs for pump, sensor and decider modules
        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.sensor.measure = MagicMock(return_value=50)
        self.decider.decide = MagicMock(return_value=1)

        self.decider.decide(self.sensor.measure(), self.pump.get_state(), self.actions)

        # Confirm that decide was called with 50, PUMP_OFF, and actions dict
        self.decider.decide.assert_called_with(50, Pump.PUMP_OFF,
                                               {'PUMP_IN': Pump.PUMP_IN,
                                                'PUMP_OUT': Pump.PUMP_OUT,
                                                'PUMP_OFF': Pump.PUMP_OFF})




class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    def setUp(self):
        self.sensor = Sensor('127.0.0.1', 8001)
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(100, .05)

        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_controller(self):
        """
        Test Controller module logic and call values
        """

        self.pump.get_state = MagicMock(return_value=Pump.PUMP_OFF)
        self.sensor.measure = MagicMock(return_value=50)
        self.decider.decide = MagicMock(return_value=1)

        self.pump.set_state = MagicMock(return_value=True)
        self.assertTrue(self.controller.tick())

        self.pump.set_state = MagicMock(return_value=False)
        self.assertFalse(self.controller.tick())



"""
C:\Users\Chris\Desktop\UW_Python\Sp2018-Online\students\ChrisH\lesson06\water-regulation-master>coverage run --include=waterregulation\controller.py,waterregulation\decider.py -m unittest waterregulation\test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK

C:\Users\Chris\Desktop\UW_Python\Sp2018-Online\students\ChrisH\lesson06\water-regulation-master>coverage report
Name                            Stmts   Miss  Cover
---------------------------------------------------
waterregulation\controller.py      11      0   100%
waterregulation\decider.py         20      0   100%
---------------------------------------------------
TOTAL                              31      0   100%

C:\Users\Chris\Desktop\UW_Python\Sp2018-Online\students\ChrisH\lesson06\water-regulation-master>
"""