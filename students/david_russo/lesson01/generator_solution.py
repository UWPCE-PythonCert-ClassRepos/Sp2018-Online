#!/usr/bin/env python

# a generator that yields a running sum of integers 
def intsum():
	running_sum = 0
	index = 0
	while True:
		yield running_sum
		index += 1
		running_sum += index


def intsum2():
	running_sum = 0
	index = 0
	while True:
		yield running_sum
		index += 1
		running_sum += index

def doubler():
	running_product = 1
	while True:
		yield running_product
		running_product *= 2

def fib():
	num1, num2 = 1, 1
	while True:
		yield num1
		num1, num2 = num2, num1 + num2

# helper function for the prime() function to determine if a number is prime
def is_prime(num):
	# if the number is even (and greater than 2), it is not prime
	if num % 2 == 0 and num > 2:
		return False
	# if num is evenly divisible by any number between 3 and itself, return false. Otherwise, return true. 
	return all(num % i > 0 for i in range(3, num))


def prime():
	candidate_num = 2
	while True:
		if is_prime(candidate_num):
			yield candidate_num
		candidate_num += 1




		
		

		
