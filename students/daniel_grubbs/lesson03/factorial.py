# Lesson 03 Assignment
# Recursion: Write a recursive solution for the factorial function
# Reference: https://www.calculatorsoup.com/calculators/discretemathematics/factorials.php

def factorial(n):
    """
    Factorial: is a function that multiplies a number by every number below it.

    Example(s):
    2 factorial - 2! = 2 x 1 = 2
    5 factorial - 5! = 5 x 4 x 3 x 2 x 1 = 120

    :return: either base case for n < 1 or n * factorial(n - 1)
    """
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test it out with assertions
def test_factorial(n):
    """
    Perform tests to validate the recursion is working when factortial(n) is run
    """
    assert 1 == factorial(1)
    assert 2 == factorial(2)
    assert 6 == factorial(3)
    assert 24 == factorial(4)
    assert 120 == factorial(5)
    assert 720 == factorial(6)


if __name__ == '__main__':
    # Test out factorial(n) using a range of numbers
    for i in range(1, 7):
        print('{}! = {}'.format(i, factorial(i)))
