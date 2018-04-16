#!/usr/bin/env python

"""
Simple Iterator modified
1) To take start, stop and step size as inputs
2) To match the functionality of range. Basically, we get a new iterator if we break mid-way through
processing the elements of the iterator.
"""


class IterateMeOne:
    """
    About as simple an iterator as you can get:
    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, start=0, stop=5, step=1):
        """
        Extra variables to keep track of initial state so that a new iterator object can be returned
        whenever a call to iter function is made.
        """
        self.initial_val_start = start

        # Variables to keep track of iterator state
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """ Return a new iterator every time a call to iter() is made """
        return IterateMeOne(self.initial_val_start, self.stop, self.step)

    def __next__(self):
        """ Magic method to compute and return the next value """
        if self.current < self.stop:
            ret_val = self.current
            self.current += self.step
            return ret_val
        else:
            raise StopIteration


if __name__ == "__main__":
    """ Main method that tests the IterateOne class """
    print("Testing the iterator")
    it = IterateMeOne(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print(i)

    for i in it:
        print(i)
