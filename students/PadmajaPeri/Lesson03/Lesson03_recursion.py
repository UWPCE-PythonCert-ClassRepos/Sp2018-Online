def factorial(number):
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    print("Factorial of zero is:{}".format(factorial(0)))
    print("Factorial of -10 is:{}".format(factorial(-10)))
    print("Factorial of 4 is:{}".format(factorial(4)))
    print("Factorial of 6 is:{}".format(factorial(6)))
    print("Factorial of 20 is:{}".format(factorial(20)))


