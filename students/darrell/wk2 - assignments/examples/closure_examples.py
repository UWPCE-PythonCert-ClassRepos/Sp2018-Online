

def multiplier(n):
    def mulitply(x):
        return x * n
    return mulitply


def test_muliplier():
    times5 = multiplier(5)
    assert times5(10) == 50

    times20 = multiplier(20)
    assert times20(10) == 200


def counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment   # don't put () here.  you are returning the function itself not the result of the function


def test_counter():

    c1 = counter(99)
    assert c1() == 100
    assert c1() == 101

    c2 = counter(5)
    assert c2() == 6
    assert c2() == 7
    assert c2() == 8


def counter_plus(start=0, step=1):
    count = start
    def increment():
        nonlocal count
        nonlocal step
        count += step
        return count
    return  increment

def test_counter_plus():
    c1 = counter_plus(100,5)
    assert c1() == 105
    assert c1() == 110
    assert c1() == 115

    c2 = counter_plus(5)
    assert c2() == 6
    assert c2() == 7
    assert c2() == 8


if __name__ == '__main__':
    test_counter()
    test_muliplier()
    test_counter_plus()