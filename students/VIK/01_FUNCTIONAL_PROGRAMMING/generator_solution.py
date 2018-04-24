#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 01 - Generators
    SUB TITLE:
      CREATOR: PydPiper
 DATE CREATED: 4/14/18
LAST MODIFIED: 4/14/18
  DESCRIPTION: Create generators for:
                sum of int (add previous to current index start from 0): 0,1,3,6,10,15
                doubler (next is double of previous: 1,2,4,8
                fibonacci (starting from 1) f(n) = f(n-1) + f(n-2): 1,1,2,3,5,8
                prime: 2,3,5,7,11

                Lesson learned here about generators is that a generator functional instance (ie my_sum = intsum())
                never steps out of the function instance upon yield. The function is executed when a next(my_sum) is
                called and "returns" or rather yields value at it's current state. When a next(my_sum) is called again
                the function instance returns to the line after yield.
                NOTE: the function itself does not have a instance (it is the reference) therefore it has no concept
                of state, it will always return the initial values
********************************************************************************************************************"""

"""FUNCTIONS"""
def intsum():
    """
    Generator: Sum of int (add previous to current index start from 0): 0,1,3,6,10,15.
    :yields: next state value. Called via next(intsum())
    """
    # reset state of the object
    start = 0
    current = start
    state = 0

    # yield enables next(object)
    while True:
        current += state
        state += 1
        yield current


# dont know why this is in the assignment test
def intsum2():
    return intsum()


def doubler():
    """
    Generator: Doubler (next is double of previous: 1,2,4,8
    :yields: next state value. Called via next(doubler())
    """
    # reset state of the object
    start = 1
    current = start

    # yield enables next(object)
    while True:
        yield current
        current *= 2


def fib():
    """
    Generator: fibonacci (starting from 1) f(n) = f(n-1) + f(n-2): 1,1,2,3,5,8
    :return: next state value. Called via next(fib())
    """
    # reset state of the object
    start1 = 1
    start2 = 1
    state = 0

    # yield enables next(object)
    while True:
        if state == 0:
            current = start1
            back2 = current
        elif state == 1:
            current = start2
            back1 = current
        else:
            current = back1 + back2
            back2 = back1
            back1 = current

        yield current
        state += 1


def prime():
    """
    Generator: prime numbers: 2,3,5,7,11
    :return: next state value. Called via next(prime())
    """
    # reset state of the object
    start = 2
    current = start
    prime = True

    # yield enables next(object)
    while True:
        for i in range(2, current):
            if current % i == 0:
                prime = False
                break
            if i == current -1:
                prime = True

        if prime == True:
            yield current
            current += 1
        else:
            current += 1


