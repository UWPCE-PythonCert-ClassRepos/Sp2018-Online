# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:56:04 2018

@author: seelc
"""

#Returns the factorial of the input parameter n
def factorial(n):
       
    if n > 1:
        return n * factorial(n-1)
    
    #Need to return 1 to correctly calculate 0!
    else:
        return 1


#Used for testing and comparing factorial values to ones on table
a = factorial(14)
print(a)
