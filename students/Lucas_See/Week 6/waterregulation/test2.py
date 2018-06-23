# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:23:20 2018

@author: seelc
"""

"""
Unit tests for the water-regulation module
"""
import os
os.chdir('C:\\Users\\seelc\\OneDrive\\Desktop\\Python\\Advanced Python\\water-regulation-master')
import logging

import unittest
from unittest.mock import MagicMock

from  pump import Pump
from sensor import Sensor
os.chdir('C:\\Users\\seelc\\OneDrive\\Desktop\\Python\\Advanced Python\\water-regulation-master//waterregulation')
import logging
from  controller import Controller
from decider import Decider

os.chdir('C:\\Users\\seelc\\OneDrive\\Desktop\\Python\\Advanced Python\\water-regulation-master')
logger = logging.getLogger('test_application')
logging.basicConfig(level=logging.DEBUG,
                        format=('%(filename)s: '    
                                '%(levelname)s: '
                                '%(funcName)s(): '
                                '%(lineno)d:\t'
                                '%(message)s')
                        )



class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class, declaring pre-requisite test objects
    outside __init__ class because I ahd difficulting using __init__
    with unittest.Testcase
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide
    
    my_pump = Pump(address, port)
    my_sensor = Sensor(address, port)
    my_decider = Decider(10,1)
    my_controller = Controller(my_sensor, my_pump, my_decider)
    address = '127.0.0.1'
    port = '8000'
    
    
    def test_first_decider(self):
        
        '''Behavior Test: If the pump is off and the height is below the margin region, then the
             pump should be turned to PUMP_IN.'''
        
        logger.info("running first decider test")

        try:
            assert(self.my_decider.decide(5, 0, self.my_controller.actions) == 1)
        except Exception as exception:
            logger.critical(exception)

        
    def test_second_decider(self):
        
        '''Behavior Test: If the pump is off and the height is above the margin region, then the
             pump should be turned to PUMP_OUT.'''
        
        logger.info("running second decider test")
        try:
            assert(self.my_decider.decide(12, 0, self.my_controller.actions) == -1)
        except Exception as exception:
            logger.critical(exception)

        
    def test_third_decider(self):
        
        '''Behavior Test: If the pump is off and the height is within the margin region or on
             the exact boundary of the margin region, then the pump shall remain at
             PUMP_OFF.'''
        
        logger.info("running third decider test")

        try:
            assert( (self.my_decider.decide(self.my_decider.target_height 
                                                      + self.my_decider.margin, 0,self.my_controller.actions))== 0)
            assert( (self.my_decider.decide(self.my_decider.target_height 
                                                      - self.my_decider.margin, 0, self.my_controller.actions))== 0)
        except Exception as exception:
            logger.critical(exception)

        
    def test_fourth_decider(self):
        
        '''Behavior Test: If the pump is performing PUMP_IN and the height is above the target
             height, then the pump shall be turned to PUMP_OFF, otherwise the pump
             shall remain at PUMP_IN.'''
        
        logger.info("running fourth decider test")
        try:
            assert( (self.my_decider.decide(self.my_decider.target_height 
                                                      + 1, 1, self.my_controller.actions)) == 0)
        except Exception as exception:
            logger.critical(exception)

        
    def test_fifth_decider(self):
        
        '''Behavior Test: If the pump is performing PUMP_OUT and the height is below the target
             height, then the pump shall be turned to PUMP_OFF, otherwise, the pump
             shall remain at PUMP_OUT.'''
        
        logger.info("running fifth decider test")
        try:
            assert( self.my_decider.decide(self.my_decider.target_height - 1, 
                                                      -1, self.my_controller.actions)== 0)
        except Exception as exception:
            logger.critical(exception)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class, declaring pump, address, etc. outside
    an __init__ method because I had some difficulty implementing __init__ while
    inhereting from unittest.Testcase
    """
    
    address = '127.0.0.1'
    port = '8000'
    my_pump = Pump(address, port)
    my_sensor = Sensor(address, port)
    my_decider = Decider(10,1)
    my_controller = Controller(my_sensor, my_pump, my_decider)
        
    def test_first_controller(self):
        
        '''Testing ability to correctly query sensor for height of tank'''
        
        logger.info("Starting first controller test")
        try:

            logger.info("Done with first controller test")
            assert( isinstance(self.my_sensor.measure(), float))
            
        except Exception as exception:
            logger.critical(exception)
            
    def test_second_controller(self):
        
        '''Tests the ability to query the pump for its current state'''
        
        logger.info("Starting second controller test")
        try:

            logger.info("Done with second controller test")
            assert( self.my_pump.get_state() in [1, -1, 0])
            
        except Exception as exception:
           logger.critical(exception)
        
        
    def test_third_controller(selft):
        
        '''Tests the ability to query the decider for the next appropriate state
        given a set of starting conditions. Note, this will only test one set of starting
        conditions. Exhaustive testing of the deciders logic is performed in DeciderTests'''
        
        try:

            logger.info("Done with third controller test")
            
            self.my_decider.decide(500, self.my_decider.target_height, self.my_controller.actions)
        except Exception as exception:
            logger.critical(exception)

        
    def test_fourth_controller(self):
        
        '''Tests the ability to set the pump to a new state'''
        try:
            logger.info("Starting fourth controller test")
            self.my_pump.set_state(0)
            assert( self.my_pump.get_state() == 0)
            
        except Exception as exception:
            logger.critical(exception)
        
    pass

if __name__ == "__main__":
    unittest.main()

