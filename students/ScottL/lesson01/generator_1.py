#!/usr/bin/env python

"""
Write a few generators
1. sum of integers
2. doubler
3. Fibonacci sequence
4. Prime numbers
"""


def sum_ints(x):
    '''
    sum of integers, keep adding the next integer
    '''

    n = 0
    for i in range(x):
        n = n + i
        yield n


def double_ints(x,y):
    '''
    Doubler, Each value is double the previous value
    '''

    for i in range(x,y):
        yield 2 ** (i-1)


def fib_seq(n):
    '''
    Fibonacci sequence up to a max value
    f(n) = f(n-1) + f(n-2)
    '''

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_list(max):
    '''
    Check for primes in range of max
    '''

    primes = []
    for n in range(2, max):
        n_prime = True
        for p in primes:
            if n%p == 0:
                n_prime = False
                break
        if n_prime:
            primes.append(n)
            yield n


if __name__ == "__main__":

    print("1. Sum of integers:")
    print(list(sum_ints(20)))

    print("2. Double the previous value:")
    print(list(double_ints(1,20)))

    print("3. Fibonacci sequence:")
    print(list(fib_seq(20)))

    print("4. Prime numbers less than 20:")
    for p in prime_list(20):
        print(p)







