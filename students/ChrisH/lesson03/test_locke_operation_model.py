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
        locke = Locke(4)
        self.assertEqual(locke.capacity, 4)

        # Test init invalid boat capacity
        for v in (0, -1):
            with self.assertRaises(ValueError):
                _ = Locke(v)

    # Test that context manager is returned
    def test_locke_enter(self):
        f = StringIO()
        locke = Locke(1)
        with redirect_stdout(f):
            cx_mgr = locke.__enter__()

        self.assertIsInstance(cx_mgr, Locke)
        self.assertIn("Stopping the pumps.", f.getvalue())
        self.assertIn("Opening the doors.", f.getvalue())

    def test_locke_exit(self):
        f = StringIO()
        locke = Locke(1)
        with redirect_stdout(f):
            locke.__exit__(None, None, None)

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
        locke = Locke(5)
        with redirect_stdout(f):
            with locke:
                locke.move_boats_through(5)
        self.assertIn("Moving 5 boats through.", f.getvalue())

        with self.assertRaises(ValueError):
            locke.move_boats_through(6)

        try:
            locke.move_boats_through(6)
        except ValueError as err:
            self.assertEqual(repr(err), "ValueError('Too many boats for locke size.',)")

        with self.assertRaises(ValueError):
            locke.move_boats_through(0)

        try:
            locke.move_boats_through(0)
        except ValueError as err:
            self.assertEqual(repr(err), "ValueError('Must send at least one boat through.',)")
