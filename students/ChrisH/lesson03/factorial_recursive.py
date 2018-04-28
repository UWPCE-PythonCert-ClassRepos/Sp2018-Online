#!/usr/bin/env python3
# -----------------------------------------------------------
# Recursive function to compute factorial of a given number.
# -----------------------------------------------------------


def recurse(num):

    if num == 0:
        return 1

    return num * recurse(num - 1)


if __name__ == "__main__":

    for n in range(10):
        print(f"Recurse {n} = {recurse(n)}")
