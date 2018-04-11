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


def prime():
    prime_numbers = []
    x = 2
    while True:
        if is_prime(x):
            prime_numbers.append(x)
            yield prime_numbers[-1]
        x += 1


def is_prime(n):
    prime_num = False
    if n in [2, 3, 5, 7]:
        return True
    for i in range(2, n):
        if n % i == 0:
            prime_num = False
            break
        else:
            prime_num = True
    return prime_num