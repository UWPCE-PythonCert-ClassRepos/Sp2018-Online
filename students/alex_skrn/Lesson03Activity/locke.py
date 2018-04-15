#!/usr/bin/env python3
"""Lesson 03 Activity -- Context Manager."""

# I don't know if the __exit__ method should return True or allow the Exception
#  raised by the move_boats_through() method propagate.


class Locke(object):
    """Very simple model of a locke operation."""

    def __init__(self, num):
        """Initialize an instance with arg num for the number of lockes."""
        self.num = num

    def __enter__(self):
        """Do nothing but print several statements."""
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        return self

    def move_boats_through(self, boats_num):
        """Do nothing but raise ValueError if arg boats exceeds limit."""
        if boats_num > self.num:
            raise ValueError("Too many boats")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Do nothing but print several statements."""
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        # return True # This handles the exception - but should it be handled?
