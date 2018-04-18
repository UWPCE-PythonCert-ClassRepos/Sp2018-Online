#!/usr/bin/env python
""" Generators for lesson 1 """


def intsum():
    """ yeild the sum of the current and the next number """
    total = 0
    next_number = 0
    while True:
        yield total
        next_number += 1
        total += next_number

def intsum2():
    """ I think I'm missing something here. I am pretty certain that I was not supposed to create this just to pass the tests.
    yield the sum of the current and the next number
    """
    total = 0
    next_number = 0
    while True:
        yield total
        next_number += 1
        total += next_number

def doubler():
    """ doubler """
    current = 1
    while True:
        yield current
        current *= 2


def fib():
    """ Fibonacci sequence """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    """
    yield prime numbers
    Generate an infinite sequence of prime numbers.
    """
    # I found this on stack overflow and really liked how clean it was.
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    D = {}
    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1



