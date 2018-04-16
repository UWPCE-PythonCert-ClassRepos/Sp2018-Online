import math

def doubler(num):
    x, y = 2, 0
    while y < num:
        yield x ** y
        y += 1

def intsum(num):
    x = 0
    y = 0
    while y < num:
        yield x
        y+=1
        x += y


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

def prime(num):
    x = 1
    y = int(math.sqrt(num) +1)
    while x < y:
        if y % x == 0:
            yield x
        x += 1