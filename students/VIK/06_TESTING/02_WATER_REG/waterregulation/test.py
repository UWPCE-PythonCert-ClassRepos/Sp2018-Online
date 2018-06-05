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

    # doneTODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide

    def setUp(self):
        sensor = Sensor(address="0.0.0.0", port=514)
        pump = Pump(address="0.0.0.0", port=514)
        decider = Decider(target_height=100, margin=0.10)
        self.controller = Controller(sensor=sensor, pump=pump, decider=decider)

    def test_init(self):
        """
        test init
        :return:
        """
        self.assertEqual(self.controller.decider.target_height, 100)
        self.assertEqual(self.controller.decider.margin, 0.10)

    def test_int_decider_pumpOFF_lowH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_IN']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=89, current_action=0,
                                                                          actions=self.controller.actions))

    def test_int_decider_pumpOFF_highH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_OUT']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=111, current_action=0,
                                                                          actions=self.controller.actions))

    def test_int_decider_pumpOFF_medH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_OFF']

        for h in range(90, 110):
            self.assertEqual(correct_response, self.controller.decider.decide(current_height=h, current_action=0,
                                                                              actions=self.controller.actions))

    def test_int_decider_pumpON_highH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_OFF']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=105, current_action=1,
                                                                          actions=self.controller.actions))

    def test_int_decider_pumpON_lowH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_IN']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=95, current_action=1,
                                                                          actions=self.controller.actions))

    def test_int_decider_pumpOUT_lowH(self):
        """
        test
        :return:
        """
        correct_response = self.controller.actions['PUMP_OFF']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=95, current_action=-1,
                                                                          actions=self.controller.actions))

    def test_int_decider_pumpOUT_highH(self):
        """"""
        test
        correct_response = self.controller.actions['PUMP_OUT']

        self.assertEqual(correct_response, self.controller.decider.decide(current_height=105, current_action=-1,
                                                                          actions=self.controller.actions))


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # doneTODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    def setUp(self):
        self.sensor = Sensor(address="0.0.0.0", port=514)
        self.pump = Pump(address="0.0.0.0", port=514)
        self.decider = Decider(target_height=100, margin=.10)
        self.controller = Controller(sensor=self.sensor, pump=self.pump, decider=self.decider)

    def test_init(self):
        """
        test
        :return:
        """
        self.assertEqual(self.controller.sensor, self.sensor)
        self.assertEqual(self.controller.pump, self.pump)
        self.assertEqual(self.controller.decider, self.decider)
        self.assertEqual(self.controller.actions['PUMP_IN'], self.pump.PUMP_IN)
        self.assertEqual(self.controller.actions['PUMP_OUT'], self.pump.PUMP_OUT)
        self.assertEqual(self.controller.actions['PUMP_OFF'], self.pump.PUMP_OFF)

    def test_tick_Acknowloedged(self):
        """
        test
        :return:
        """
        self.controller.sensor.measure = MagicMock(return_value=89)
        self.controller.pump.get_state = MagicMock(return_value=0)
        self.controller.pump.set_state = MagicMock(return_value=True)

        self.assertTrue(self.controller.tick())

    def test_tick_NOTAcknowloedged(self):
        """
        test
        :return:
        """
        self.controller.sensor.measure = MagicMock(return_value=89)
        self.controller.pump.get_state = MagicMock(return_value=0)
        self.controller.pump.set_state = MagicMock(return_value=False)

        self.assertFalse(self.controller.tick())
