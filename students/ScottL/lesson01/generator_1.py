#!/usr/bin/env python

"""
Write a few generators
1. sum of integers
2. doubler
3. Fibonacci sequence
4. Prime numbers
"""

import math


def intsum():
    '''
    sum of integers, keep adding the next integer
    '''

    n = 0
    the_sum = 0
    while True:
        yield the_sum
        print(the_sum)
        n += 1
        the_sum += n


def doubler():
    '''
    Doubler, Each value is double the previous value
    '''

    i = 1
    the_double = 1
    while True:
        yield the_double
        print(the_double)
        i += 1
        the_double = 2 ** (i - 1)



def fib():
    '''
    Fibonacci sequence generator
    f(n) = f(n-1) + f(n-2)
    '''

    a, b = 1, 1
    while True:
        yield a
        print(a)
        a, b = b, a + b


def prime():
    '''
    Prime number generator
    '''
    count = 2
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            yield(count)
            print(count)
        count += 1