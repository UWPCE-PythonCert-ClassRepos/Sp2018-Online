def factorial(number):
	if number != 1:
		return number*factorial(number-1)
	return 1

if __name__ == "__main__":
	print(factorial(1))
	print(factorial(2))
	print(factorial(3))
	print(factorial(4))
