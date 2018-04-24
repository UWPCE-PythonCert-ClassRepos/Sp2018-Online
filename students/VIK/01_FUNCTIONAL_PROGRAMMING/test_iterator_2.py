#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 01 - Iterators - Unitest
    SUB TITLE: Iterators vs Range
      CREATOR: PydPiper
 DATE CREATED: 4/14/18
LAST MODIFIED: 4/14/18
  DESCRIPTION: Test class against range(). Note: makes use of double iterable in single for loop via zip
********************************************************************************************************************"""

"""IMPORTS"""
import unittest
import iterator_2 as it2


"""GLOBAL VARIBALES"""
myR = range(2, 20, 2)
myI = it2.Iterator_2(2, 20, 2)


"""TEST"""
class MyTest(unittest.TestCase):
    def test_1st_pass_half_forloop(self):
        for r, i in zip(myR, myI):
            if r and i > 10:
                self.assertEqual(r, i)

    def test_1st_pass_finish_forloop(self):
        for r, i in zip(myR, myI):
            self.assertEqual(r, i)

"""MAIN"""
if __name__ == "__main__":
    unittest.main()
