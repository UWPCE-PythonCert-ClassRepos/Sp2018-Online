#!/usr/bin/env python3
# Lesson 03 Activity
# Context Managers: Ballard Lockes
import sys

class Locke(object):
    """
    Simulate the overall functioning of the Ballard Locke system.
    """
    def __init__(self, number_of_boats=1):
        """
        Constructor for the Locke class
        """
        self.number_of_boats = number_of_boats

    def __enter__(self):
        """
        When the locke is entered it stops the pumps, opens the doors,
        closes the doors, and restarts the pumps.
        """
        print("\nOpening with '__enter__' method.")
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Starting the pumps.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        When the locke is exited it runs through the same steps as __enter__
        it stops the pumps, opens the doors, closes the doors, and restarts the pumps.

        exc_type, exc_val, exc_tb are associated with exception handling
        """
        print("\nClosing with '__exit__' method.")
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Starting the pumps.")

    def boats_through_locke(self, boats):
        """Move the boats through."""
        if boats > self.number_of_boats:
            sys.exit("Too many boats are trying to pass through the locke.")
        print("{} boats allowed to pass through the locke.".format(boats))


if __name__ == '__main__':
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Context managers
    with small_locke as locke:
        locke.boats_through_locke(boats)

    with large_locke as locke:
        locke.boats_through_locke(boats)
