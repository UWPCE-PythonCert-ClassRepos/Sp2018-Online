#!/usr/bin/env python

#-------------------------------------------------#
# Title: factorial_function
# Dev: Scott Luse
# Date: April 21, 2018
#-------------------------------------------------#

"""
Write a recursive solution for the factorial function.

"""

def factorial(x):
    '''
    Function returns factorial of input
    Uses a termination condition of one
    '''
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def test_factorial():
    flist = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
    nlist = []
    print("\n"+"Running factorial test 1-11")
    print("=====================================")
    for i in range(1,12):
        nlist.append(factorial(i))
        print(list(nlist))
    assert flist == nlist



def main():
    test_factorial()


if __name__ == "__main__":
    main()

