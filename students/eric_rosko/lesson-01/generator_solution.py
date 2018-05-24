#!/usr/bin/env python3

'''
Name:       generator_solution.py
Author:     Eric Rosko
Date:       Apr 8, 2018
Python ver. 3.4.3
'''
'''
One does not directly write a generator in Python 2.2+. Instead, one writes a function that, when called, returns a generator.
A generator does not need an __iter__() statement, it returns value with a yeield which
stops program flow, it resumes when next is called again.
'''

def intsum():
    print("start")
    current = 0
    previous = 0
    while True:
        print("in while")
        yield current + previous
        previous = current + previous
        current += 1


def intsum2():
    print("start")
    current = 0
    previous = 0
    while True:
        print("in while")
        yield current + previous
        previous = current + previous
        current += 1


def doubler():
    current = 0
    while True:
        yield 2**current
        current += 1


def fib():
    previous = -1
    current = 1
    while True:
        if previous == -1:
            previous = 0
            yield 1
        else:
            yield current + previous
            temp = previous + current
            previous = current
            current = temp


def prime():
    current = 2
    failed = False
    while True:
        if current == 2:
            current += 1
            yield 2
        for num in range(2, current - 1):
            print("looping...", num, current)
            if current % num == 0:
                failed = True
                print(current, "is not prime with", num)

        if failed == False:
            print("found prime", current)
            yield current
        current += 1
        failed = False



if __name__ == "__main__":
    func = prime()
    print(next(func))
    print(next(func))
    print(next(func))
    # print(next(func))

    # for i in range (3):
    #     print(i)

    # for i in range(2, 5):
    #     print("at range", i)
    #     temp = next(func)
    #     print("temp", temp)
    # func = intsum()
    # for i in range(5):
    #     print("at range", i)
    #     temp = next(func)
    #     print("temp", temp)
