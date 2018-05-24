#!/usr/bin/env python3

import itertools as it


class intsum(object):

    def __init__(self):
        self.current = 0
        self.next = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.next += 1
        self.current += self.next
        return self.current


def intsum2():
    current = 0
    next_num = 0
    while True:
        current += next_num
        yield current
        next_num += 1


def intsum3():
    for x in it.accumulate(it.count()):
        yield x


def doubler():
    for dblr in it.accumulate(it.count(1), lambda x, y: x*2):
        yield dblr


def fib():
    # Set first two in sequence as 1,0, which will correctly produce 1, 1, 2 ...
    p = 1
    q = 0

    while True:
        yield p + q
        p, q = q, p + q


def prime():
    # somewhat inefficient prime number generator using a list comprehension
    # skips even numbers
    yield 2
    num = 3
    while True:
        if not [d for d in range(3, num, 2) if num % d == 0]:
            yield num
        # else:
        #    print(num, [d for d in range(3, num, 2) if num % d == 0])
        num += 2




