#!/usr/bin/env python3

"""Lesson 03 -- Recursion."""

def rec_factorial(x):
    """Return the factorial of x calculated recursively."""
    if x == 0:
        return 1
    else:
        return x * rec_factorial(x-1)


# Testing the recursive factorial function
assert rec_factorial(5) == 120
assert rec_factorial(10) == 3628800
