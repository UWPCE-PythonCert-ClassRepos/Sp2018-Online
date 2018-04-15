# Python Cert, lesson 2, Closures

from string import ascii_lowercase
from functools import partial
from itertools import chain
from itertools import count
from itertools import tee


# Closures (most simple)
def outer_funct():
    message = "Hi"

    def inner_funct():
        print(message)

    return inner_funct()


outer_funct()


def outer_funct2():
    message = "Hello"

    def inner_funct2():
        print(message)

    return inner_funct2


# Notice how this was created as a function, not a variable! then you call the function
new_funct = outer_funct2()
new_funct()


# Same thing with passing arguments
def outer_funct3(msg):
    message = msg

    def inner_funct3():
        print(message)

    return inner_funct3


new_funct2 = outer_funct3("Nice to meet you")
new_funct2()


# Another Closure Example

def make_multiplier(n):

    def multiply(x):
        return print(n * x)

    return multiply


times3 = make_multiplier(4)
times3(5)


# Currying

def crazy(a, b, c, d=2, e=1):
    return print(a * b * c * d * e)


crazy(5, 4, 3)

crazy_part = partial(crazy, d=4, e=2)
crazy_part(1, 1, 1)


# Itertools

# creating our data
myletters = [letters for letters in ascii_lowercase]
mynumbers = [number for number in range(len(myletters))]
print(myletters)
print(mynumbers)

# Chaining them together in a list
mychain = chain(myletters, mynumbers)
print(*mychain)

# Showing that this is an iterator
mychain = chain(myletters, mynumbers)
print(next(mychain))
print(next(mychain))
print(next(mychain))
print(*mychain)

# Zipping them together
mychain = chain(myletters, mynumbers)
print(*zip(count(), mychain))


# Making duplicated with tee
mychain1, mychain2 = tee(mychain)

print(*mychain1)
print('')
print(*mychain2)

# We can also use the functions directly in tee
mychain3, mychain4 = tee(chain(myletters, mynumbers))
print(*mychain3)
print('')
print(*mychain4)
