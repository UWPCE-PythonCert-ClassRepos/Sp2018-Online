#!/usr/bin/env python3

'''
Name:       iterator_2.py
Author:     Eric Rosko
Date:       Apr 8, 2018
Python ver. 3.4.3
'''

from iterator_1 import IterateMe_1

class IterateMe_2(IterateMe_1):

    def __init__(self, start, stop, step=1):
        self.current = -1
        self.start = start
        self.stop = stop
        self.step = step


# adding this make it behave like range
    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        if self.current == -1:
            self.current = self.start
        else:
            self.current += self.step

        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration



if __name__ == "__main__":
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)
    for i in it:
        print(i)


    aRange = range(10)
    for i in aRange:
        if i > 5:  break
        print(i)
    for i in aRange:
        print(i)
