# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:40:49 2018

@author: seelc
"""

'''Exploring option 1 in activity 10: Using memoization to improve code performance,
will try both an object oriented and non object oriented memoization approach and 
compare performance between versions'''


from timeit import default_timer as timer
from great_circle_v0 import great_circle
import logging

logging.basicConfig(level=logging.INFO)

def memoize(input_func):
    
    '''memoize function to keep track of of values returned from input_func'''
    
    func_list = {}
    def helper(i):
        
        '''helper func to check if call of input_func returns a value currently
        in func_list, if not returns'''
        
        if i not in func_list:            
            func_list[i] = input_func(i)
        return func_list[i]
    
    return helper

    
def exponential_series(n):
    
    '''Recrusive power series that takes the intial n value and calls the
    function recursively n-1 times'''

    if n == 1:
        return 1
    else:
        return exponential_series(n - 1) * 2


class oop_memoize:
    
    '''Object oriented memoization approach'''
    
    def __init__(self, function):
        self.function = function
        self.call_storage = {}
    
    def __call__(self, *args):
        
        '''Using same approach as in "helper" function, adding function values
        to storage if not already in it'''
        
        if args not in self.call_storage:
            self.call_storage[args] = self.function(*args)
        return self.call_storage[args]
        
@oop_memoize        
def oop_exponential_series(n):

    '''Same as "exponential_series", just adding decorator'''
    
    if n == 1:
        return 1
    else:
        return oop_exponential_series(n - 1) * 2

    
if __name__ == "__main__":
    iterations = 10
    
    #calling and timing exponential function without a helper
    start1 = timer()
    my_func = exponential_series(iterations)
    end1 = timer()
    run_time_base = end1 - start1
    
    start2 = timer()
    my_func = memoize(exponential_series(iterations))
    end2 = timer()
    run_time_memoize = end2 - start2
    
    difference = run_time_memoize/run_time_base
    print("Percentage run time reduction, memoization: ", difference)
    #Strategy results in almost a halving of the total run time with iterations = 20
    
    #Now testing object oriented memoiation method
    start3 = timer()
    my_oop_func = oop_exponential_series(iterations)
    end3 = timer()
    run_time_oop_memoize = end3 - start3
    difference2 = run_time_oop_memoize/run_time_base
    print("Percentage run time reduction oop memoize: ", difference2)
    
    '''For some reasone the object oriented memoization method is taking significantly
    longer than the base version, not sure if this is because theres some overhead
    associated with setting up a class or if I made an error in my code'''
    