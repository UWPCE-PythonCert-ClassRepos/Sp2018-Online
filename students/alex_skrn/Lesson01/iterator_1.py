#!/usr/bin/env python

"""
Simple iterator examples
"""

# Task summary:
# Part 1: Extend IterateMe_1 to be more like range() – add three input
#  parameters: iterator_2(start, stop, step=1)
# Part 2: Make iterator_2 more like range() (i.e., in my understanding,
# not consumable)

# Question: is range an iterator or an iteratable?
# My answer: range() has no next method, so it is not an iterator;
# Furthermore, if it is passed to iter() function, you get
# a range_iterator object, so it should be a kind of iterable


# Initial example provided as part of the assignment - MY CODE IS BELOW IT
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


# MY SOLUTION - Option 1 - with start, stop, step=1
class IterateMe_2:
    """Create an iterable object. A very simplified version of range().

    three input parameters: start, stop, step=1
    __iter__ but not __next__ is implemented
    to make objects of this class inexhaustable like in range()
    """

    def __init__(self, start, stop, step=1):
        """Parameters: start, stop (assume > start), step (defaults to 1)."""
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Implement iter."""
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


# MY SOLUTION - Option 2 - with start, stop=None, step=1
class IterateMe_3:
    """Create an iterable object. A very simplified version of range().

    three input parameters: start, stop=None, step=1
    __iter__ but not __next__ is implemented
    to make objects of this class inexhaustable like in range()
    """

    def __init__(self, start, stop=None, step=1):
        """Parameters: start, stop (defaults to None), step (defaults to 1)."""
        if stop is None:
            self.start, self.stop = 0, start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        """Implement iter."""
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


if __name__ == "__main__":

    # print("Testing the iterator")
    # for i in IterateMe_1():
    #     print(i)

    print("Testing IterateMe_2 -- accepts 2 or 3 args, not consumable")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print(i)

    for i in it:
        print(i)

    print(list(it))

    print("Testing IterateMe_3 -- now accepts 1, 2, or 3 args, not consumable")
    it3a = IterateMe_3(10)
    it3b = IterateMe_3(2, 20, 2)
    print(list(it3a))
    print(list(it3b))
    print(list(it3b))
