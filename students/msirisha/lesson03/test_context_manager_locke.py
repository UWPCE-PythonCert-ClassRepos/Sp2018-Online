#!/usr/bin/env python3
import unittest
import context_manager_locke as cm
from io import StringIO
from contextlib import redirect_stdout


class ContextManagerTests(unittest.TestCase):
    def setUp(self):
        self.locke = cm.Locke(5)

    def test_cm_locke_init(self):
        self.assertEqual(self.locke.capacity, 5)

        with self.assertRaises(ValueError):
            _ = cm.Locke(0)

        with self.assertRaises(ValueError):
            _ = cm.Locke(-1)

    def test_cm_locke_enter(self):
        # https://docs.python.org/3/library/contextlib.html
        f = StringIO()
        with redirect_stdout(f):
            self.locke.__enter__()
        self.assertIn('Stopping the pumps', f.getvalue())
        self.assertIn('Opening the doors', f.getvalue())
        self.assertIn('Closing the doors', f.getvalue())
        self.assertIn('Restarting the pumps', f.getvalue())

    def test_cm_locke_exit(self):
        # https://docs.python.org/3/library/contextlib.html
        f = StringIO()
        with redirect_stdout(f):
            self.locke.__exit__(None, None, None)
        self.assertIn('Stopping the pumps', f.getvalue())
        self.assertIn('Opening the doors', f.getvalue())
        self.assertIn('Closing the doors', f.getvalue())
        self.assertIn('Restarting the pumps', f.getvalue())

    def test_move_boats_through_for_small_locke(self):
        boats = 4
        f = StringIO()
        with redirect_stdout(f):
            self.locke.move_boats_through(boats)
        # stripping new line characters
        self.assertEqual("Moving {} boats through".format(boats), f.getvalue().strip())

    def test_move_boats_through_for_large_locke(self):
        boats = 8
        with self.assertRaises(ValueError):
            self.locke.move_boats_through(boats)

    def test_move_boats_through_for_zero_negative_locke_size(self):
        boats = 0

        with self.assertRaises(ValueError):
            self.locke.move_boats_through(boats)

        boats = -1

        with self.assertRaises(ValueError):
            self.locke.move_boats_through(boats)

    def test_move_boats_through_exception_message(self):
        try:
            self.locke.move_boats_through(8)
        except ValueError as e:
            self.assertEqual(repr(e), "ValueError('Too many boats for locke',)")


if __name__ == "__main__":
    unittest.main()
