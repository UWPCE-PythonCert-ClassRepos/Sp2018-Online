#!/usr/bin/env python3

import math as mt

def doubler():
    current = 1
    while True:
        yield current
        current *= 2


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


def intsum(num):
    x = 0
    y = 0
    while y < num:
        yield x
        y+=1
        x += y

# I absolutely hated this one. Thank god for stack overflow
def primes():
    ps, cur = [2], 3
    yield 2
    while True:
        y = int(mt.sqrt(cur))
        c = next((x for x in ps if cur % x == 0), None)

        if c == None:
            yield cur
            ps.append(cur)

        cur += 2