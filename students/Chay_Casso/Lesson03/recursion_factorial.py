#!/usr/bin/env python3
#
# Recursion Factorial
# Chay Casso, 4/22/18

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

print(factorial(42))