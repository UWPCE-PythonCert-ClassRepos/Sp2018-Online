def doubler(max):
    x, y = 2, 0
    while y < max:
        yield x ** y
        y += 1

def intsum(max):
    x, y = 0
    while y < max:
        yield x
        y+=1
        x += y

def fib(max):
    x, y = 0, 1
    while x < max:
        yield x
        x, y = y, x + y

def prime(max):
    x = 1
    while x < max:
        if x % 2 != 0 or x == 2:
            yield x
        x += 1

def main():
        int_sum = doubler(10)
        for x in int_sum:
            print(x)

if __name__ == "__main__":
    main()