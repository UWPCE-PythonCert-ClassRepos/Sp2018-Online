import itertools


def sum_of_integers(start=0):
    """
    Generator that returns sum of integers. Every call adds the next integer in the
    sequence to the previously stored sum and returns it.
    Starting value is 1.
    """
    current = start
    sum_val = 0
    while True:
        sum_val += current
        yield sum_val
        current += 1


def doubler():
    """
    Generator that returns a value which is the twice the previous returned value.
    First value returned is 1.
    """
    product = 1
    while True:
        yield product
        product *= 2


def fibonacci():
    """
    Generator that yields one term in the fibonacci sequence when invoked. Any term in the sequence is computed as
    the sum of previous 2 terms. The first 2 values in the sequence are 1, 1.
    """
    first_term = 0
    second_term = 1
    num_term = 1
    while True:
        sum_val = first_term + second_term
        yield sum_val
        num_term += 1
        if num_term > 2:
            """
            The first 2 terms are 1. We want to assign the new values to first
            and second term only from the 3rd term.
            """
            first_term, second_term = second_term, sum_val


def prime_numbers():
    numbers = itertools.count(start=2, step=1)  # Prime numbers start with 2.
    for num in numbers:
        # Find out if the number has a divisor in range 2 and num/2
        divisor_range = range(2, int(num / 2) + 1)
        for divisor in divisor_range:
            if num % divisor == 0:
                break
        else:
            # We checked all divisors. The number is a prime. Return it.
            yield num


if __name__ == '__main__':
    prime_num = prime_numbers()
    print(next(prime_num))
    print(next(prime_num))
    print(next(prime_num))
    print(next(prime_num))
    print(next(prime_num))
    print(next(prime_num))
    print(next(prime_num))
