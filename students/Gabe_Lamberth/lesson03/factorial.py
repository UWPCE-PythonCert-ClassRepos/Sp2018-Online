#!/usr/bin/env python3


# Creating recursive function to print a factorial of 5

def factorial_recurssion(num):
    if num > 1:
        return num * factorial_recurssion(num -1)
    else:
        return 1


# Using range to build factorial number with input of 5
def factorial_range(num):
    prod =1
    for x in range(1, num+1):
        prod *= x
    return prod




def main():

    print('The result of factorial 5 with recursion function is =', factorial_recurssion(5))
    print()
    print('The result of factorial 5 with range function is =', factorial_range(5))


if __name__ == "__main__":
    main()
