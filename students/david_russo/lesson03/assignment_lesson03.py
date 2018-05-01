#!/usr/bin/env python

def factorial(n):
	"""
	The factorial function takes an integer input of n and returns the product of itself and the n-1 
	integers less than n. 
	"""
	if n < 0:
		raise ValueError("You must enter an integer greater than or equal to 0. ")
	elif n == 0 or n == 1:
		return 1
	else:
		return n*factorial(n-1)
