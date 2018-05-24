def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

assert(factorial(3)==6)
print(factorial(3))
assert(factorial(4)==24)
print(factorial(4))