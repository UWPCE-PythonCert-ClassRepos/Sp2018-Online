"""
This module performs a unittest on timeit_experiment to make sure all methods return the same values
"""

from unittest import TestCase
from timeit_experiment import *


class AllTests(TestCase):
    """
    This class tests all methods from the timeit exercise to make sure they return the same values
    """
    def test_all_equal(self):
        a = map_filter_with_functions_func(multiply_by_two, greater_than_lower_limit, my_list)
        b = map_filter_with_lambdas_func(my_lower_limit, my_list)
        c = comprehension_func(my_lower_limit, my_list)
        d = comprehension_with_lambdas_func(my_lower_limit, my_list)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(a, d)

