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
    next = 0
    while True:
        current += next
        yield current
        next += 1


def intsum3():
    for x in it.accumulate(it.count()):
        yield x


def doubler():
    for dblr in it.accumulate(it.count(1), lambda x, y: x*2):
        yield dblr


def fib():
    p = 0
    q = 1

    yield 1

    while True:
        yield p + q
        p, q = q, p + q

