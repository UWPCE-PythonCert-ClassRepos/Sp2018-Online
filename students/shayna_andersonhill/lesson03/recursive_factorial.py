
def recursive_factorial(number):
    if number == 0 or number == 1:
        factorial = 1
        return factorial
    else:
        factorial = number * recursive_factorial(number - 1)
        return factorial
