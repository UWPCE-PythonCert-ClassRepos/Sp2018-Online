"""
Module tests for the water-regulation module
"""

import logging
import os
import unittest
from unittest.mock import MagicMock
os.chdir('C:\\Users\\seelc\\OneDrive\\Desktop\\Python\\Advanced Python\\water-regulation-master')
#from pump import Pump
#from sensor import Sensor

os.chdir('C:\\Users\\seelc\\OneDrive\\Desktop\\Python\\Advanced Python\\water-regulation-master//waterregulation')
from controller import Controller
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

class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """
    
        # TODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.

        
    Pump = MagicMock()
    Pump_methods = {'set_state.return_value': True, 'get_state.return_value': 1}
    Pump.configure_mock(**Pump_methods)
    Pump = Pump
    logger.info(Pump.set_State(), Pump.get_State())
    print(Pump.set_state())
    print(Pump.get_state())
            
            
    logger.info("Creating mocked sensor")
    Sensor = MagicMock()
    Sensor_methods = {'measure.return_value': 4.0}
    Sensor.configure_mock(**Sensor_methods)
    Sensor = Sensor
    print(Sensor.measure())
    
    def integration_test(self):
        
        '''Uses mocked Sensor and Pump as inputs into a decider and controller,
        tests controller output for given inputs'''
        
        '''For the integration check we are only checking the end result of our function calls,
        in this case the ability to correctly return true from teh set_state function with
        the previous functions as inputs'''
        
        actions = {'PUMP_IN' : 1,
                   'PUMP_OFF' : 0,
                   'PUMP_OUT' : -1
                }
        logger.info("Begininning integration_test")
        my_decider = Decider(5.0,1)
        my_controller = Controller(self.Sensor, self.Pump, my_decider)
        print(my_decider.decide(self.Sensor.measure(), self.Pump.get_state, actions))
        
        #Tick Behavior 4
        assert my_controller.Pump.set_state(my_decider.decide(self.Sensor.measure(),
                                                              self.Pump.get_state, actions)) == True
        #Final check
        assert my_controller.tick() == None
        
 
    #pass


if __name__ == "__main__":
    unittest.main()