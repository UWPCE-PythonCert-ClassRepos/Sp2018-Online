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
from Factorial import factorial as ft

class MyTest(unittest.TestCase):
    def test_5(self):
        self.assertEqual(120, ft(5))

    def test_10(self):
        self.assertEqual(3628800, ft(10))

    def test_limits(self):
        with self.assertRaises(MemoryError):
            ft(1000)


if __name__ == "__main__":
    unittest.main()
