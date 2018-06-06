"""Lesson 10 - Profiling & Perfomance -- Memoization etc.

Task: Explore code-only performance improvement strategies such as memoization.

This code uses examples from Chapter 18.5 of Python Cookbook, O'Reilly;
Introduction to computation and programming using Python, MIT Press;
stackoverflow.com;
www.python-course.eu/python3_memoization.php
"""

from timeit import timeit as timer

repititions = 10000
fib_num = 15


def rec_fib_simple(n):
    """Calculate nth fib number using simple recursion."""
    if n == 0 or n == 1:
        return n
    else:
        return rec_fib_simple(n-1) + rec_fib_simple(n-2)


def rec_fib_inner_rec_func(n):
    """Calculate nth fib number using recursion - a better implementation."""
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)


def iter_fib(n):
    """Calculate nth fib number using iteration -- for loop."""
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


def iter_fib2(n):
    """Calculate nth fib number using iteration -- while loop."""
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def gen_fib(n):
    """Calculate nth fib number using a generator and a for loop."""
    def fib():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b
    f = fib()
    for i in range(n):
        res = next(f)
        if i == n - 1:
            return res


def rec_fib_inner_memo(n, memo={}):
    """Calculate nth fib number using recursion and an internal memo."""
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        memo[n] = result = rec_fib_inner_memo(n-1, memo) + rec_fib_inner_memo(n-2, memo)
        return result


fib_memo = {}


def rec_fib_ext_memo(n):
    """Calculate nth fib number using recursion and an external memo."""
    if n == 0 or n == 1:
        return n
    if n not in fib_memo:
        fib_memo[n] = rec_fib_ext_memo(n-1) + rec_fib_ext_memo(n-2)
    return fib_memo[n]


def memoize(f):
    """Create a closure to encapsulate the memoization mechanism."""
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def rec_fib_inner_rec_func_decorator(n):
    """Calculate nth fib number using recursion - a better implementation."""
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)


class Memoize:
    """Encapsulate the caching in a class."""

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def rec_fib_inner_rec_func_decorator_class(n):
    """Calculate nth fib number using recursion - a better implementation."""
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)


print("\n\nrecursive_fib_simple")
# print("check the fib num is always the same:", rec_fib_simple(fib_num))
print(timer(
    """recursive_fib_simple = rec_fib_simple(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrec_fib_inner_recursive_func")
# print("check the fib num is always the same:", rec_fib_inner_rec_func(fib_num))
print(timer(
    """recursive_fib_inner_recur_func = rec_fib_inner_rec_func(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\ngenerator_and_for_loop_fib")
# print("check the fib num is always the same:", gen_fib(fib_num))
print(timer(
    """generator_fib = gen_fib(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\niterative_fib_with_for_loop")
# print("check the fib num is always the same:", iter_fib(fib_num))
print(timer(
    """iterative_fib = iter_fib(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\niterative_fib_with_while_loop")
# print("check the fib num is always the same:", iter_fib2(fib_num))
print(timer(
    """iterative_fib2 = iter_fib2(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrecursive_fib_internal_memo")
# print("check the fib num is always the same:", rec_fib_inner_memo(fib_num))
print(timer(
    """recursive_fib_inner_memo = rec_fib_inner_memo(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrecursive_fib_external_memo")
# print("check the fib num is always the same:", rec_fib_ext_memo(fib_num))
print(timer(
    """recursive_fib_ext_memo = rec_fib_ext_memo(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrecursive_fib_memo_decorator_function")
# print("check the fib num is always the same:", rec_fib_inner_rec_func_decorator(fib_num))
print(timer(
    """recursive_fib_memo_decorator_memoize = rec_fib_inner_rec_func_decorator(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )

print("\n\nrecursive_fib_memo_decorator_class")
# print("check the fib num is always the same:", rec_fib_inner_rec_func_decorator_class(fib_num))
print(timer(
    """recursive_fib_memo_use_class = rec_fib_inner_rec_func_decorator_class(fib_num)""",
    globals=globals(),
    number=repititions
            )
      )
