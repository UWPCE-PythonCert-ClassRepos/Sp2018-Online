#Using recursion for factorial
#if 0, factorial is 1

def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#procedural factorial
def factorial_p(n):
    f=1
    for i in range (1, n+1):
        f = f * i
    return f

#Test with Fibonacci
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)
 #   if n == 1:
 #       return 1
 #   elif n == 2
 #       return 1
 #   elif n > 2:
 #       return

fib_cache = {}
def fib_mem(n):
    #retrun cached value
    if n in fib_cache:
        return fib_cache[n]
    #calculate Nth
    #elif value = 1 if n < 3 else fib(n - 1) + fib(n - 2)
    #cache the value and return it
    fib_cache[n] = value
    return value

#testing
#factorial 0 == 1, 2 == 2, 6==720

assert factorial(6) == 720
assert factorial (2) == 2
assert factorial (0) == 1