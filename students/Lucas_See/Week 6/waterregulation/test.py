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
    Unit tests for the Decider class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide


    def first_decider_test(self, address, port):
        
        '''Behavior Test: If the pump is off and the height is below the margin region, then the
             pump should be turned to PUMP_IN.'''
        
        logger.info("running first decider test")
        my_pump = Pump(address, address)
        my_sensor = Sensor(address, port)
        my_decider = Decider(10,1)
        my_controller = Controller(my_sensor, my_pump, my_decider)
        try:
            self.assertequals(my_decider.decide(5, 0, my_controller.actions), 1)
        except Exception as exception:
            logger.critical(exception)

        
    def second_decider_test(self, address, port):
        
        '''Behavior Test: If the pump is off and the height is above the margin region, then the
             pump should be turned to PUMP_OUT.'''
        
        logger.info("running second decider test")
        my_pump = Pump(address, port)
        my_sensor = Sensor(address, port)
        my_decider = Decider(10,1)
        my_controller = Controller(my_sensor, my_pump, my_decider)
        try:
            self.assertequals(my_decider.decide(12, 0, my_controller.actions), -1)
        except Exception as exception:
            logger.critical(exception)

        
    def third_decider_test(self, address, port):
        
        '''Behavior Test: If the pump is off and the height is within the margin region or on
             the exact boundary of the margin region, then the pump shall remain at
             PUMP_OFF.'''
        
        logger.info("running third decider test")
        my_pump = Pump(address, port)
        my_sensor = Sensor(address, port)
        my_decider = Decider(10,1)
        my_controller = Controller(my_sensor, my_pump, my_decider)
        try:
            self.assertequals( my_decider.decide(my_decider.target_height + my_decider.margin, 0,my_controller.actions), 0)
            self.assertequals( my_decider.decide(my_decider.target_height - my_decider.margin, 0, my_controller.actions), 0)
        except Exception as exception:
            logger.critical(exception)

        
    def fourth_decider_test(self, address, port):
        
        '''Behavior Test: If the pump is performing PUMP_IN and the height is above the target
             height, then the pump shall be turned to PUMP_OFF, otherwise the pump
             shall remain at PUMP_IN.'''
        
        logger.info("running fourth decider test")
        my_pump = Pump(address, port)
        my_sensor = Sensor(address, port)
        my_decider = Decider(10,1)
        my_controller = Controller(my_sensor, my_pump, my_decider)
        try:
            self.assertequals( my_decider.decide(my_decider.target_height + 1, 1, my_controller.actions), 0)
        except Exception as exception:
            logger.critical(exception)

        
    def fifth_decider_test(self, address, port):
        
        '''Behavior Test: If the pump is performing PUMP_OUT and the height is below the target
             height, then the pump shall be turned to PUMP_OFF, otherwise, the pump
             shall remain at PUMP_OUT.'''
        
        logger.info("running fifth decider test")
        my_pump = Pump(address, port)
        my_sensor = Sensor(address, port)
        my_decider = Decider(10,1)
        my_controller = Controller(my_sensor, my_pump, my_decider)
        try:
            self.assertequals( my_decider.decide(my_decider.target_height - 1, -1, my_controller.actions), 0)
        except Exception as exception:
            logger.critical(exception)


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """
    

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick
    
    def first_controller_test(self, address, port):
        
        '''Testing ability to correctly query sensor for height of tank'''
        
        logger.info("Starting first controller test")
        try:
            #Creating pump, sensor, and decider for test case
            my_pump = Pump(address, port)
            my_sensor = Sensor(address, port)
            my_decider = Decider(10,1)
            #Passing pump, sensor, and decider to controller
            my_controller = Controller(my_sensor, my_pump, my_decider)
            logger.info("Done with first controller test")
            self.asserttrue( isinstance(my_sensor.measure(), float))
            
        except Exception as exception:
            logger.critical(exception)
            
    def second_controller_test(self, address, port):
        
        '''Tests the ability to query the pump for its current state'''
        
        logger.info("Starting second controller test")
        try:
            #Creating pump, sensor, and decider for test case
            my_pump = Pump(address, port)
            my_sensor = Sensor(address, port)
            my_decider = Decider(10,1)
            #Passing pump, sensor, and decider to controller
            my_controller = Controller(my_sensor, my_pump, my_decider)
            logger.info("Done with second controller test")
            self.assertTrue( my_pump.get_state() in [1, -1, 0])
            
        except Exception as exception:
           logger.critical(exception)
        
        
    def third_controller_test(self, address, port):
        
        '''Tests the ability to query the decider for the next appropriate state
        given a set of starting conditions. Note, this will only test one set of starting
        conditions. Exhaustive testing of the deciders logic is performed in DeciderTests'''
        
        if True:
            logger.info("Starting third controller test")
            #Creating pump, sensor, and decider for test case
            my_pump = Pump(address, port)
            my_sensor = Sensor(address, port)
            my_decider = Decider(10,1)
            #Passing pump, sensor, and decider to controller
            my_controller = Controller(my_sensor, my_pump, my_decider)
            logger.info("Done with third controller test")
            
            my_decider.decide(500, my_decider.target_height, my_controller.actions)
        #except Exception as exception:
            #logger.critical(exception)
        
    def fourth_controller_test(self, address, port):
        
        '''Tests the ability to set the pump to a new state'''
        try:
            logger.info("Starting fourth controller test")
            print("here")
            #Creating pump, sensor, and decider for test case
            my_pump = Pump(address, port)
            my_sensor = Sensor(address, port)
            my_decider = Decider(10,1)
            #Passing pump, sensor, and decider to controller
            my_controller = Controller(my_sensor, my_pump, my_decider)
            logger.info("Done with fourth controller test")
            my_pump.set_state(0)
            self.assertequal( my_pump.get_state(), 0)
            
        except Exception as exception:
            logger.critical(exception)
        
    def create_instance(address, port, target_height, margin):
        
        '''helper method to create new pump, sensor, decider, and controller
        for each test'''
        
        my_pump = Pump(address, port)
        my_sensor = Sensor(address, port)
        my_decider = Decider(target_height,margin)
        #Passing pump, sensor, and decider to controller
        my_controller = Controller(my_sensor, my_pump, my_decider)
        
        logger.info("succesfully created controller instance")
        
    pass

if __name__ == "__main__":
    
    '''Creates new controller test objects and runs through all the given controller
    test methods'''
    
    unittest.main()
    address = '127.0.0.1'
    port = '8000'
    my_controller_tests = ControllerTests()
    my_controller_tests.first_controller_test(address, port)
    my_controller_tests.second_controller_test(address, port)
    my_controller_tests.third_controller_test(address, port)
    my_controller_tests.fourth_controller_test(address, port)
    
    my_decider_test = DeciderTests()
    my_decider_test.first_decider_test(address, port)
    my_decider_test.second_decider_test(address, port)
    my_decider_test.third_decider_test(address, port)
    my_decider_test.fourth_decider_test(address, port)
    my_decider_test.fifth_decider_test(address, port)
    
    
    
