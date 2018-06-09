def intsum():
	"""
	Sum of the integers
	"""
	total = 0
	i = 0
	while True:
		yield total
		i += 1
		total += i

def intsum2():
	"""
	Sum of the integers
	"""
	total = 0
	i = 0
	while True:
		yield total
		i += 1
		total += i

def doubler():
	"""
	Doubler
	"""
	res = 1
	while True:
		yield res
		res *= 2

def fib():
	"""
	Fibonacci sequence
	"""
	temp1, temp2 = 1, 1
	while True:
		yield temp1
		temp1, temp2 = temp2, temp1 + temp2

def prime():
	"""
	Prime number sequence
	"""
	i = 2
	while True:
		if is_prime_number(i):
			yield i
		i += 1

def is_prime_number(number):
	if number >= 2:
		for x in range(2,number):
			if not (number%x):
				return False
	else:
		return False 
	return True

