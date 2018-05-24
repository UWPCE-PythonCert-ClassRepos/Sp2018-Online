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

# After watching the video on Slack -
#  - there was a hint to reset self.current in __iter__
class IterateMe_22:
    def __init__(self,  start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


# Here goes my previous solutions

# OPTION 1 - with start, stop, step=1
class IterateMe_2:
    """Create an iterable inexhaustable range-like object.

    three input parameters: start, stop, step=1
    __iter__ but not __next__ is implemented
    to make objects of this class inexhaustable like range()
    """

    def __init__(self, start, stop, step=1):
        """Parameters: start, stop (assume > start), step (defaults to 1)."""
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Implement iter with yield statement."""
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


# OPTION 2 - with start, stop=None, step=1, reverse possible, e.g. (10, 0, -1)
class IterateMe_3:
    """Create an iterable inexhaustable range-like object.

    three input parameters: start, stop=None, step=1
    __iter__ but not __next__ is implemented
    to make objects of this class inexhaustable like range()
    """

    def __init__(self, start, stop=None, step=1):
        """Parameters: start, stop (defaults to None), step (defaults to 1)."""
        if stop is None:
            self.start, self.stop = 0, start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        # Some safeguards to avoid an infinite loop in case of illegal input,
        # eg. (10, 1, 1), (1, 10, -1)
        if self.start < self.stop:
            assert self.step > 0, "Need a positive Step here"
        if self.start > self.stop:
            assert self.step < 0, "Need a negative Step here"


    def __iter__(self):
        """Implement iter with yield statement."""
        n = self.start
        # while n < self.stop:
        while n != self.stop:
            yield n
            n += self.step


# OPTION 3 -- using 2 separate classes to create a range-like object
# This more complicated solution is offered on
# https://anandology.com/python-practice-book/iterators.html
# Author's note: "if both iteratable and iterator are the same object,
# it is consumed in a single iteration."
# I modified the author's code to handle several input parameters
# and cases like zrange(10, -1, -1)

class zrange:
    """Create an iterable inexhaustable range-like object."""

    def __init__(self, start, stop=None, step=1):
        """Parameters: start, stop (defaults to None), step (defaults to 1)."""
        if stop is None:
            self.start, self.stop = 0, start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        """Return an iterator created by zrange_iter class."""
        return zrange_iter(self.start, self.stop, self.step)


class zrange_iter:
    """Probvide an iterator object for zrange class."""

    def __init__(self, start, stop, step):
        if start < stop:
            assert step > 0, "Need a positive Step here"
        if start > stop:
            assert step < 0, "Need a negative Step here"
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start != self.stop:
            i = self.start
            self.start += self.step
            return i
        else:
            raise StopIteration()


if __name__ == "__main__":

    # print("Testing the iterator")
    # for i in IterateMe_1():
    #     print(i)

    print("Testing IterateMe_22 -- after watching slack video")
    it22 = IterateMe_22(2, 20, 2)
    for i in it22:
        if i > 10:
            break
        print(i)

    for i in it22:
        print(i)

    print(list(it22))
    print(list(it22))

    print()

    print("Testing IterateMe_2 -- accepts 2 or 3 args, not consumable")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print(i)

    for i in it:
        print(i)

    print(list(it))
    print(list(it))

    print()

    print("Testing IterateMe_3 -- 1, 2, or 3 args, not consumable, reverse")
    it3a = IterateMe_3(10)
    it3b = IterateMe_3(2, 20, 2)
    print(list(it3a))
    print(list(it3a))
    print(list(it3b))
    print(list(it3b))

    it3c = IterateMe_3(20, 2, -2)
    print(list(it3c))
    print(list(it3c))

    print()

    print("Testing zrange -- up to 3 args, not consumable, reverse possible")
    z = zrange(5)
    print(list(z))
    print(list(z))
    z2 = zrange(2, 20, 2)
    print(list(z2))
    print(list(z2))
    z3 = zrange(20, 2, -2)
    print(list(z3))
    print(list(z3))
    assert list(zrange(2, 2)) == []
    z4 = zrange(3, -1, -1)
    assert list(z4) == [3, 2, 1, 0]
    assert list(z4) == [3, 2, 1, 0]
