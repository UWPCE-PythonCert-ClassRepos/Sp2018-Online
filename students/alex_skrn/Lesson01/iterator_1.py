#!/usr/bin/env python

"""
Simple iterator examples
"""


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


class IterateMe_2:
    """Create an iterable object. A very simplified version of range()."""

    def __init__(self, start, stop, step=1):
        """Assume start < stop."""
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Make objects of this class inexhaustable like range()."""
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


class IterateMe_3:
    """Create an iterable object. A very simplified version of range()."""

    def __init__(self, start, stop=None, step=1):
        """Assume start < stop."""
        if stop is None:
            self.start, self.stop = 0, start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        """Make objects of this class inexhaustable like range()."""
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

    print("Testing IterateMe_3 -- now accepts 1 or 2 or 3 args")
    it3a = IterateMe_3(10)
    it3b = IterateMe_3(2, 20, 2)
    print(list(it3a))
    print(list(it3b))
