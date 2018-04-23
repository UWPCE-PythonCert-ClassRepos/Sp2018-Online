def intsum():
    """
    Sum of integers
    keep adding the next integer
    0 + 1 + 2 + 3 + 4 + 5 + …
    so the sequence is:
    0, 1, 3, 6, 10, 15 …..
    """
    sum = 0
    i = 0
    while True:
        sum += i
        yield sum
        i += 1


def intsum2():
    """
    Sum of integers
    keep adding the next integer
    0 + 1 + 2 + 3 + 4 + 5 + …
    so the sequence is:
    0, 1, 3, 6, 10, 15 …..
    """
    sum = 0
    i = 0
    while True:
        sum += i
        yield sum
        i += 1


def doubler():
    """
    Each value is double the previous value:
    1, 2, 4, 8, 16, 32,
    """
    a = 1
    while True:
        yield a
        a *= 2


def fib():
    """
    Fibonacci series with generators
    1 1 2 3 5 8 13 21 34 55..
    :return: a number in fibonacci series
    """
    first = 1
    second = 1
    while True:
        yield first
        first, second = second, first + second


def isprime(n):
    """ Checks whether given number is prime or not """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime():
    """
    Returns prime numbers. Implemented using generators.
    :return:  Prime number
    """
    n = 2
    while True:
        if isprime(n):
            yield n
        n += 1


