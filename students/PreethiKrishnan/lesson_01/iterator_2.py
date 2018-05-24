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

    def __init__(self, start, stop, increment):
        self.current = -1
        self.stop = stop
        self.start = start
        self.increment = increment

    def __iter__(self):
        #self.current = -1 if this is used here after break it does not pick up where it left off after initial break in for loop. If uncommented it starts from first as if it was initialized again
        return self


    def __next__(self):
        self.current += self.increment
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    final_iterate = IterateMe_1(2, 25, 2)
    for i in final_iterate:
        print(i)
    #What happens if there is a break??
    final_iterate = IterateMe_1(2, 25, 2)
    for i in final_iterate:
        if i > 10:
            break
        print("This is inside break: {}".format(i))
    #Here after break it starts from where it left off in previous for loop
    for i in final_iterate:
        print("After break without re-initializing: {}".format(i))
    print("Range is not an iterator")
