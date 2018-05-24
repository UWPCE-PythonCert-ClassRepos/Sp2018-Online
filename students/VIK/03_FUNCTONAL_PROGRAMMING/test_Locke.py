#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 03 - Activity - Unitest
    SUB TITLE: Boats through a Lock - using context management
      CREATOR: PydPiper
 DATE CREATED: 4/21/18
LAST MODIFIED: 4/21/18
  DESCRIPTION: Test each functional def
********************************************************************************************************************"""

"""IMPORTS"""
import unittest
import Locke as Lo
from io import StringIO
import sys
from contextlib import contextmanager

"""TEST DATA"""
small_locke = Lo.Locke(5)
large_locke = Lo.Locke(10)
FP_small_locke = Lo.FP_Locke(5)
FP_large_locke = Lo.FP_Locke(10)

boats = 8


"""CMD OUTPUTS"""
@contextmanager
def cmd_outputs():
    """
    Context Manager: Use with "with cmd_outputs as out:",
    Redirects cmd outputs to StringIO() that can be retrieved via .getvalue()
    Note: use out.getvalue().split("\n") to separate multiple print statements
    :return: None, resets sys.stdout upon close()
    """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


class MyTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(small_locke.capacity, 5)

    def test_normal(self):
        with cmd_outputs() as out:
            with large_locke as mylocke:
                mylocke.move_boats_through(boats)
            message = "Lock has sufficient capacity for the boats."
            self.assertIn(message, out.getvalue().split("\n"))

    def test_overlimit(self):
        with cmd_outputs() as out:
            with small_locke as mylocke:
                mylocke.move_boats_through(boats)
            message = "Bound Exception Found: Too many boats through a small locke."
            self.assertIn(message, out.getvalue().split("\n"))

    def test_FP_init(self):
        self.assertIn(5, FP_small_locke.args)

    def test_FP_normal(self):
        with cmd_outputs() as out:
            with FP_large_locke as mylocke:
                mylocke.move_boats_through(boats)
            message = "Lock has sufficient capacity for the boats."
            self.assertIn(message, out.getvalue().split("\n"))

    def test_FP_overlimit(self):
        with cmd_outputs() as out:
            with FP_small_locke as mylocke:
                mylocke.move_boats_through(boats)
            message = "Bound Exception Found: Too many boats through a small locke."
            self.assertIn(message, out.getvalue().split("\n"))


if __name__ == "__main__":
    unittest.main()
