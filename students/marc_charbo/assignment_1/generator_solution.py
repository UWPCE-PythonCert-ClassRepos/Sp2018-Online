
def intsum(i):
    x = i
    while True:
        yield x
        x += i

def main():
        x = intsum(1)
        print (next(x))
        print(next(x))
        print(next(x))
        print(next(x))

if __name__ == "__main__":
    main()