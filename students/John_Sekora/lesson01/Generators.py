# John Sekora
# Class 2, Lesson01, Generators
# UW Certificate in Python, 4/9/2018


def intsum():
    """ Sum of integers """
    # 0 + 1 + 2 + 3 + 4 + 5 + …
    # so the next sequence is:
    # 0, 1, 3, 6, 10, 15 ...
    current_integer = 0
    current_sum = 0
    while True:
        yield current_sum
        current_integer += 1
        current_sum += current_integer


def intsum2():
    """ Sum of integers """
    # 0 + 1 + 2 + 3 + 4 + 5 + …
    # so the next sequence is:
    # 0, 1, 3, 6, 10, 15 ...
    current_integer = 0
    current_sum = 0
    while True:
        yield current_sum
        current_integer += 1
        current_sum += current_integer


def doubler():
    ''' Doubler'''
    # Each value is double the previous value:     1, 2, 4, 8, 16, 32...
    current_number = 1
    while True:
        yield current_number
        current_number *= 2


# Fibonacci Sequence
def fib():
    ''' The Fibonacci Sequence '''
    # f(n) = f(n-1) + f(n-2)
    #  1, 1, 2, 3, 5, 8, 13, 21, 34
    x = 1
    y = 1
    while True:
        yield x
        x, y = y, x + y


# Prime Numbers
def prime_set(x):
    ''' Prime Numbers '''
    # Generate the prime numbers (numbers only divisible by them self and 1):
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 …
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
            else:
                return True


def prime():
    n = 2
    while True:
        yield n
        n += 1
        while True:
            if prime_set(n):
                break
            else:
                n += 1
                continue

