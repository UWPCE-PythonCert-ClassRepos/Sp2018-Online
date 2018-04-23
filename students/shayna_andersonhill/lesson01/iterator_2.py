#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_2:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, start, stop, step=1):
        #self.current = -1
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start 
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_2(2, 20, 2)

#When I break the loop and try and pick it up again, 
#the loop starts up after the broken iteration
    for i in it: 
        if i >10: break
        print(i)

#Make yours match range() 
#Strategy: reinitialize it after a break
    it = IterateMe_2(2, 20, 2) 

    for i in it:
        print(i)

#Range behaves differently becausse it does not "remember" 
#the state of of the iterator
    print("Testing range function for comparison")
    for i in range(2, 20, 2):
        if i > 10: break
        print(i)

    for i in range(2, 20, 2):
        print(i)

#Question: Is range() an iterator or an iterable?

#My Answer: Since you need a function to iterate over range()
#I think that range() is an iterable and not an iterator in 
#and of itself. 
#Proof: When you try and call next over a range, you get the
#TypeError: 'range' object is not an iterator




