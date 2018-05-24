#!/usr/bin/env python3

# Recursive solution for python factorial


def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Number should be >=0, factorial for {} can not be evaluated".format(n))
    else:
        return n * fact_recursive(n - 1)


if __name__ == "__main__":
    for i in range(-1, 6, 1):
        try:
            print("factorial for number {} is {}".format(i, fact_recursive(i)))
        except ValueError as e:
            print("exception is {}".format(e))
