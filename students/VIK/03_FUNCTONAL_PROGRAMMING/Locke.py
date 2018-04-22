#!/usr/bin/python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 03 - Activity
     SUB TITLE: Boats through a Lock - using context management
       CREATOR: PydPiper
  DATE CREATED: 4/21/18
 LAST MODIFIED: 4/21/18
   DESCRIPTION: Create a class Locke that has:
                __init__: takes the capacity of boats per locke
                __enter__: prints "Stopping the pump."
                                  "Opening the doors."
                                  "Closing the doors."
                                  "Restarting the pumps."
                move_boats_through(boats) method: if locke capacity < boats raise an error
                __exit__: prints same as enter
********************************************************************************************************************"""

"""IMPORTS"""
from contextlib import contextmanager

# OOP Version: context manager class
class Locke(object):

    def __init__(self, capacity):
        """
        Stores Locke's capacity
        :param capacity: int, number of boats a Locke can hold
        """
        self.capacity = capacity

    def __enter__(self):
        """
        Start 'with Class as something" context
        :return: a subclass with an attribute of class.move_boats_through
        """
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")

        # returned class needs to pass __init__ capacity info
        return WithinContext(self.capacity)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close context
        :param exc_type: exception type (error raised)
        :param exc_val: exception: error value/message
        :param exc_tb: traceback of exception, if True
        :return:
        """
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        if exc_type == ValueError:
            print("Bound Exception Found: Too many boats through a small locke.")
            return True
        else:
            print("Unbound Exception Found!")
            return False

# FP version
@contextmanager
def FP_Locke(capacity):
    # __init__ equivalent
    try:
        # __enter__ equivalent
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        yield WithinContext(capacity)
    except ValueError:
        print("Bound Exception Found: Too many boats through a small locke.")
    finally:
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")


class WithinContext(object):
    def __init__(self, capacity):
        self.capacity = capacity

    def move_boats_through(self, boats):
        """
        Method to check if Locke is large enough to let boats through
        :param boats: boats passing through Locke
        :return: None or ValueError if Locke capacity is insufficient
        """
        if boats > self.capacity:
            raise ValueError
        else:
            print("Lock has sufficient capacity for the boats.")
