#sum of integers: keep adding the next integer
def intsum(n=0):
    adder = 0
    while True:
        yield n + adder
        n = n + adder
        adder += 1


#doubler: each value is double the previous value
def doubler(n=1):
    while True:
        yield n
        n = n * 2

#fibonacci sequence: f(n) = f(n-1) + f(n-2)
def fib(n1=1, n2=1):
    n3 = 0
    while n3 < 2:
        yield 1
        n3 += 1
    while True:
        yield n3
        n1 = n2
        n2 = n3
        n3 = n1 + n2 

#prime numbers: numbers only divisible by themself and one
def prime(n=2):
    while True:
        while n == 2:
            yield 2
            n += 1
        for i in range(2, n):
            if n % i == 0:
                n += 1
                break
        else:
            yield n
            n += 1

if __name__ == "__main__":
    tester = prime()
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
    print(next(tester))
