#!/usr/bin/env python3

"""A lab on generators."""

# from math import sqrt

# MY COMMENT:
# I don't understand what test_intsum2() in test_generator.py is for.
# This function's code is the same as that of test_intsum().
# And I don't see any relevant task in the assignment.


def intsum():
    """Sum of integers."""
    # Keep adding the next integer
    # 0 + 1 + 2 + 3 + 4 + 5 + …
    # so the sequence is: 0, 1, 3, 6, 10, 15 ….
    current_sum = 0
    current_int = 0
    while True:
        yield current_sum
        current_int += 1
        current_sum += current_int


def doubler():
    """Each value is double the previous value: 1, 2, 4, 8, 16, 32,."""
    current_val = 1
    while True:
        yield current_val
        current_val *= 2


def fib():
    """Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34,."""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    """Generate prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23,."""
    # def is_prime(x):
    #     """See if x is prime by Trial Division."""
    #     for i in range(2, int(sqrt(x)) + 1):
    #         if x % i == 0:
    #             return False
    #     return True
    #
    # is_prime() below does the same is above but with a while loop to avoid
    # having to import math.sqrt
    def is_prime(x):
        """See if x is prime by Trial Division."""
        d = 2  # the initial divisor to try
        while d * d <= x:  # do until divisor becomes sqrt of x (in worst case)
            if x % d == 0:
                return False
            d += 1
        return True
    # start the sequence with 2
    prime = 2
    while True:
        yield prime
        prime += 1
        while True:
            if is_prime(prime):
                break
            else:
                prime += 1
