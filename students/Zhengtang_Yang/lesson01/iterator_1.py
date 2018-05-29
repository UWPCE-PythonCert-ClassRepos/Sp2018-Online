#!/usr/bin/env python

"""
Simple iterator examples
"""

import math

class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)

class iterator_2:
    """
    range() is an iterable because it does not save state or have the next() method
    """

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        return math.ceil((self.stop - self.start)/self.step)

    def __getitem__(self, input1):
        """
        This is the method for iteration
        """
        if input1 >= len(self):
            raise IndexError("Range Out of Index")
        return self.start + self.step*input1

if __name__ == "__main__":
    print('Case 1')
    it = iterator_2(2,20,2)
    for i in it:
        if i > 10: break
        print(i)

    print('Case 2')
    it0 = range(2,20,2)
    for i in it0:
        if i > 10: break
        print(i) 

    print('Case 3')
    for i in range(2,20,2):
        print(i)

    print('Case 4')
    for i in it:
        print(i)