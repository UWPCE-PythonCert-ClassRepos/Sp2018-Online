#!/usr/bin/env python

"""
Simple iterator examples
"""
import math

class IterateMe_2:
    """
    This is an iterable, but not an iterator. One difference between iterables
    and iterators is that iterators have __next__ methods while iterables do 
    not. 
    """

    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError("Range out of index")
        return self.start + self.step*item

    def __len__(self):
        return math.ceil((self.stop - self.start)/self.step)


if __name__ == "__main__":
    print("-"*50)
    print("Testing IterateMe_2")
    for i in IterateMe_2(2, 20, 2):
        print(i)

    print("-"*50)
    print("Testing breaking IterateMe_2")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10: break
        print(i)

    print("-"*50)
    print("Resume iterating over the iterator it")
    for i in it:
        print(i)

    print("-"*50)
    print("Testing breaking range(2, 20, 2)")
    it_range = range(2, 20, 2)
    for i in it_range:
        if i > 10: break
        print(i)

    print("-"*50)
    print("Resume iterating over range(2, 20, 2)")
    for i in it_range:
        print(i)

    print("-"*50)
    print("Since range() does not remember state, it is an iterable (and not an iterator).")






