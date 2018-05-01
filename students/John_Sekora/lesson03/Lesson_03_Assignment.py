# Write a recursive solution for the factorial function


def fac(n):
    ''' Factorial Function '''
    mul = 1
    while n >= 1:
        mul = mul * n
        n = n - 1
    return mul


def fac_recursive(n):
    ''' Factorial Function (Recursive) '''
    if n == 0:
        return 1
    else:
        return n * fac_recursive(n-1)


if __name__ == '__main__':
    print("file ran directly")

