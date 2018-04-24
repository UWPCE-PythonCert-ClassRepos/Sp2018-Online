#!/usr/bin/env python

import activity_lesson03 as activity03
import unittest


class activity_lesson03_test(unittest.TestCase):
	# test boat threshold if number of boats exceeds locke size
	def test_max_boats_exceed(self):	
		# create a locke of capacity 10
		locke10 = activity03.Locke(10)

		# ensure that moving 11 boats through the locke raises an error
		self.assertRaises(ValueError, locke10.move_boats_through, 11)

	# test boat threshold if number of boats is less than locke size
	def test_max_boats_no_exceed(self):
		# create a locke of capacity 100
		locke100 = activity03.Locke(100)
		locke100.move_boats_through(99)

		# ensure that moving 99 boats does not raise an error
		self.assertEqual(locke100.number_of_boats, 99)

if __name__ == '__main__':
    unittest.main() 
