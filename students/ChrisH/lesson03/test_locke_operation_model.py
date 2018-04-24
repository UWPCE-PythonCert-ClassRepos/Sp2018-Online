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


    # Test return error value from close()

    # Test that context manager is returned
    def test_locke_enter(self):
        f = StringIO()
        l = Locke(1)
        with redirect_stdout(f):
            cx_mgr = l.__enter__()

        self.assertIsInstance(cx_mgr, Locke)
        self.assertIn("Stopping the pumps.", f.getvalue())
        self.assertIn("Opening the doors.", f.getvalue())

    def test_locke_exit(self):
        f = StringIO()
        l = Locke(1)
        with redirect_stdout(f):
            cx_mgr = l.__exit__(None, None, None)

        self.assertIsInstance(cx_mgr, Locke)
        self.assertIn("Closing the doors.", f.getvalue())
        self.assertIn("Restarting the pumps.", f.getvalue())

    def test_locke_context_manager_basic(self):
        f = StringIO()
        with redirect_stdout(f):
            with Locke(1):
                pass
        self.assertIn("Stopping the pumps.", f.getvalue())
        self.assertIn("Opening the doors.", f.getvalue())
        self.assertIn("Closing the doors.", f.getvalue())
        self.assertIn("Restarting the pumps.", f.getvalue())

    def test_locke_move_boats_through(self):
        f = StringIO()
        l = Locke(5)
        with redirect_stdout(f):
            with l:
                l.move_boats_through(5)
        self.assertIn("Moving 5 boats through.", f.getvalue())

        with redirect_stdout(f):
            with l:
                try:
                    l.move_boats_through(65)
                except ValueError:
                    self.assertIn("Too many boats for locke size.", f.getvalue())



'''

small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

#Too many boats raises exception:
locke.move_boats_through(boats)

# Sufficent capacity moves boats w/out incident.
'''

