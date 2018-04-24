#!/usr/bin/env python

import assignment_lesson03 as assignment03
import unittest


class assignment_lesson03_test(unittest.TestCase):
	# test boat threshold if number of boats exceeds locke size
	def test_factorial_negative(self):	
		self.assertRaises(ValueError, assignment03.factorial, -1)

	def test_factorial_zero(self):
		self.assertEqual(1, assignment03.factorial(0))

	def test_factorial_one(self):
		self.assertEqual(1, assignment03.factorial(1))

	def test_factorial_five(self):
		self.assertEqual(120, assignment03.factorial(5))

	def test_factorial_seven(self):
		self.assertEqual(5040, assignment03.factorial(7))


if __name__ == '__main__':
    unittest.main() 