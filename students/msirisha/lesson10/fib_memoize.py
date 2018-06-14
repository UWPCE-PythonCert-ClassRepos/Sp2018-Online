
""" Lesson 10 Memoization example
https://www.python-course.eu/python3_memoization.php
"""

from timeit import timeit as timer

repititions = 10000
fib_number = 15


def rec_fib_simple_example(n):
    """ Calculate nth fib number using simple recursion """
    if n == 0 or n == 1:
        return n
    else:
        return rec_fib_simple_example(n-1) + rec_fib_simple_example(n-2)


def rec_fib_inner_rec_fun(n):
    """ Calculates nth fib number using inner recursion """
    def inner_fib(a, b, n):
        return inner_fib(b, a+b, n-1) if n > 0 else a
    return inner_fib(0, 1, n)


def iter_fib(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


def generator_fib(n):
    """ Calculates the fibonacii series using """
    def fib():
        a, b = 1,1
        while True:
            yield a
            a, b = b, a +b
    f = fib()
    for i in range(n):
        res = next(f)
        if i == n-1:
            return res


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper

@memoize
def fib_inner_func_rec_decorator(n):
    def fib_help(a, b, n):
        return fib_help(b, a +b, n-1) if n > 0 else a
    return fib_help(0, 1, n)


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
            return self.memo[args]

@memoize
def fib_inner_func_rec_decorator_class(n):
    def fib_help(a, b, n):
        return fib_help(b, a +b, n-1) if n > 0 else a
    return fib_help(0, 1, n)


print("\n\nrec_fib_simple_example")
print(timer(
    """recursive_fib_simple = rec_fib_simple_example(fib_number)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrec_fib_inner_rec_fun")
print(timer("""rec_fib_inner_rec_fun_example = rec_fib_inner_rec_fun(fib_number)""", globals=globals(),number=repititions))


print("\n\niter_fib")
print(timer("""iteration_fib = iter_fib(fib_number)""", globals=globals(),number=repititions))

print("\n\ngenerator_fib")
print(timer("""generator_fib_example = generator_fib(fib_number)""", globals=globals(), number=repititions))


print("\n\nfib_inner_func_rec_decorator")
print(timer("""fib_inner_func_rec_decorator_example = fib_inner_func_rec_decorator(fib_number)""", globals=globals(),
            number=repititions))

print("\n\nfib_inner_func_rec_decorator_class")
print(timer(
    """fib_inner_func_rec_decorator_class_example = fib_inner_func_rec_decorator_class(fib_number)""",
    globals=globals(),
    number=repititions
            )
      )




