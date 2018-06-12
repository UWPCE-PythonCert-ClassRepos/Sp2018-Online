def fx(x):
    return x ** 2


def trap_int(start, stop, dx):
    result = 0
    steps = round((stop - start) / dx)
    x1 = start
    for i in range(steps):
        x2 = x1 + dx
        x1 = x2
        result += ((fx(x1) + fx(x2)) / 2)*dx
    return result
