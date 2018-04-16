# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:21:43 2018

@author: seelc
"""
from Iterate1 import IterateMe_1 

class IterateMe_2(IterateMe_1):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, start, stop, step=1):
        self.step = step
        self.stop = stop
        self.start = start
        self.current = 0

    def __iter__(self):
        
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

#Testing Iterator versus range, while I added the additional arguments to 
#__init__ the iterator still resumes from where it left off after break is called
if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)
    print("break")    
    for i in it:
        print(i)
      
    it2 = range(2, 20, 2)
    for i in it2:
        if i > 10:  break
        print(i)
        
    for i in it2:
        print(i)