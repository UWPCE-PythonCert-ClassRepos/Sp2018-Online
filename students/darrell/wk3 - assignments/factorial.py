# def fac(n):
#     # print(n)
#     return 1 if (n == 0) else n * fac(n-1)


def fac(n):
    if n == 0:
        return 1
    else:
       # print('stack{})'.format(n))
       return n * fac(n-1)


assert fac(5) == 120
assert fac(10) == 3628800
