# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:29:34 2018

@author: seelc
"""

import math

#Sums all previous numbers
def sum_of():
    result = 0
    summation = 0
    while True:
        print(summation)
        result += 1
        yield summation
        summation = summation + result
    
a = sum_of()
next(a)

#doubles each previous number
def doubler():
    first = 1
    while True:
        yield first
        first = first*2
        
b = doubler()
#next(b)

#Fibonnaci sequence function
def fibonnaci():
    first = 1
    yield first
    second = 1
    yield second
    while True:
        third = first + second
        first = second
        second = third
        yield third

c= fibonnaci()
#next(c)

def prime():
    n  = 0
    while True:
        if math.factorial(n) % (n + 1) == n and n != 0: 
           next_prime = ((math.factorial(n) % (n + 1)) / n) * (n - 1) + 2
           yield next_prime
           n = n + 1
        else:
            n = n + 1
            
d = prime()  

def x_squared():
    x = 0
    while True:
        result = x**2
        
        yield result
        x = x + 1
        
e = x_squared()

    
def x_to_the_third():
    x = 0
    while True:
        result = x**3
        
        yield result
        x = x + 1

f = x_to_the_third()
       
def x_by_three():
    x = 0
    while True:
        yield x
        x = x + 3
g = x_by_three()    
    
def x_by_minus_seven():
    x = 0
    while True:
        yield x
        x = x - 7

h = x_by_minus_seven()
    
    
    
    
    
    
    