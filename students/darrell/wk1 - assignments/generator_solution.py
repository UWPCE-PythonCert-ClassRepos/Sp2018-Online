import math


def intsum():
    seq =[0]
    while True:
        if len(seq) == 1:
            yield 0
        else:
            yield sum(seq)
        seq.append(seq[-1] + 1)


def doubler():
    n = 1
    while True:
        if n == 1:
            yield 1
        else:
            yield n
        n *= 2

def fib():
    seq = [1]
    while True:
        yield seq[-1]
        if len(seq) == 1:
            seq.append(1)
        else:
            # add the last 2 numbers in seq and append
            seq.append(sum(seq[-2:]))


def intsum():
    seq =[0]
    while True:
        if len(seq) == 1:
            yield 0
        else:
            yield sum(seq)
        seq.append(seq[-1] + 1)


def doubler():
    n = 1
    while True:
        if n == 1:
            yield 1
        else:
            yield n
        n *= 2

def fib():
    seq = [1]
    while True:
        yield seq[-1]
        if len(seq) == 1:
            seq.append(1)
        else:
            # add the last 2 numbers in seq and append
            seq.append(sum(seq[-2:]))

def prime():
    prime_numbers = []
    x = 2
    while True:
        if is_prime(x):
            prime_numbers.append(x)
            yield prime_numbers[-1]
        x += 1


def is_prime(n):

    if n == 1:
        return False
    if n in [2, 3, 5, 7]:
        return True
    # exclude even numbers and numbers divisible by 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # only test 6k +- 1 <= sqrt(n)
    for i in -1, 1:
        x = 6 + i
        while x <= math.sqrt(n):
            if n % x == 0:
                return False
            x += 6
    return True




