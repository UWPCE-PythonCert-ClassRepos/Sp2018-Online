#!/usr/bin/env python3
# -----------------------------------------------------------
#  uses unittest module to test locke_operation_model class module
# -----------------------------------------------------------

import unittest
from io import StringIO
from contextlib import redirect_stdout
from locke_operation_model import Locke


class LockeTest(unittest.TestCase):

    def test_locke_init(self):

        # Test simple init
        L = Locke(4)
        self.assertEqual(L.capacity, 4)

        # Test init invalid boat capacity
        for v in (0, -1):
            with self.assertRaises(ValueError):
                L = Locke(v)


    # Test return value from close()

    # Test that context manager is returned



'''
Expected output lines
"Stopping the pumps."
"Opening the doors."
"Closing the doors."
"Restarting the pumps."


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

#Too many boats raises exception:
locke.move_boats_through(boats)

# Sufficent capacity moves boats w/out incident.
'''

