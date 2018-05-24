"""recursive.py"""
import sys


def my_fun(n):
    if n == 2:
        return True

    return my_fun(n / 2)


if __name__ == '__main__':
    n = 19
    print(my_fun(n))
