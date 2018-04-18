#!/usr/bin/env python3

'''
Name:       test_iterator_2.py
Author:     Eric Rosko
Date:       Apr 8, 2018
Python ver. 3.4.3
'''

from iterator_2 import *

def test_iterator_2():
    for item in IterateMe_2(0, 5, 2):
        print("test_iterator_2", item)


# Q: What happens if you break from a loop and try to pick it up again:
# A: Since the instance persists between uses, it maintains its internal
# state.


