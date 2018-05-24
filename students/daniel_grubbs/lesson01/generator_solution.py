"""
Create generators for the following:
- Sum of integers
- Doubler
- Fibonacci sequence
- Prime numbers
"""
import math

def intsum(start=0):
    total = start
    for i in range(20):
        total += i
        yield total


def intsum2(start=0):
    total = start
    i = start
    while True:
        total += i
        yield total
        i += 1


def doubler(start=1):
    """Double the number."""
    d = start
    while True:
        yield d
        d = d * 2


def fib():
    """Fibonacci Series"""
    # Starting numbers in series are n1, n2
    n1 = 0
    n2 = 1

    yield n2 # needs to be outside the loop

    while True:
        # yield n2
        next_num = n1 + n2
        yield next_num
        n1 = n2
        n2 = next_num



def prime(start=2):
    """Prime numbers. Prime numbers exclude the number 1."""
    total = start
    if total == 2:
        yield total

    while True:
        total += 1
        for prime in range(2, total + 1):
            if prime == total:
                yield prime
            else:
                break






