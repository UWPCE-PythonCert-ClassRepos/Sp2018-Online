#!/usr/bin/env python3
"""Write a recursive solution for the factorial function.
https://en.wikipedia.org/wiki/FactorialLinks to an external site."""


def factorial(number):
    if number < 0:
        raise ValueError("number must not be negative")
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
