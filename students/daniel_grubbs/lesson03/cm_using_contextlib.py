#!/usr/bin/env python3
"""
Creating a Context Manager using contextlib

Reference: Python 201: Intermediate Python by Michael Driscoll

The contextlib module allows us to create a context manager using contextlib's contextmanager function as a
decorator.

- Use it to open and close a file.
"""
from contextlib import contextmanager
import os

@contextmanager
def file_open(path):
    """Open file."""
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error")
    finally:
        print("Closing file")
        f_obj.close()

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = "{}/test.txt".format(dir_path)
    with file_open(file) as fobj:
        fobj.write("Testing context manager")