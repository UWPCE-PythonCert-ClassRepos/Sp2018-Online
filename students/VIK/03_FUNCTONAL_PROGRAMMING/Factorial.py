#!/usr/bin/python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 03 - Assignment
     SUB TITLE: Factorial - recursion
       CREATOR: PydPiper
  DATE CREATED: 4/21/18
 LAST MODIFIED: 4/21/18
   DESCRIPTION: Create a function recursion for mathematical factorials
                ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
********************************************************************************************************************"""


def factorial(val):
    """
    Recursive Function: mathematical factorial (!number)
    :param val: int, may not exceed 999 stacks
    :return: int, factorial
    """
    if val == 1000:
        raise MemoryError("Max Stack Warning: Recursion may not exceed 1000 stacks")
    if val == 0:
        return 1
    else:
        return val * factorial(val - 1)

