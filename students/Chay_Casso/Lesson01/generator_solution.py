#!/usr/bin/env python3
#
# Generators
# Chay Casso
# 4/9/2018

from itertools import *


def intsum():
    return accumulate(count())


def intsum2():
    return accumulate(count())


def doubler():
    return map(lambda x: 2**x, count())

def fibonacci(n):
    """Return the nth fibonacci sequence number."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fib():
    return map(lambda n: fibonacci(n), count(2))

def prime_run(x):
    for i in range(2, x):
        if x % i == 0: return False
    else: return True

def prime():
    return filter(lambda x: prime_run(x), count(2))
