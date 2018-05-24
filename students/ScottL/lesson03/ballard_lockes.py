#!/usr/bin/env python

#-------------------------------------------------#
# Title: ballard_lockes
# Dev: Scott Luse
# Date: April 22, 2018
#-------------------------------------------------#

"""
Operating Ballard Lockes with Context Manager

"""


class Locke():

    def __init__(self, capacity ):
        self.size = capacity
        self.boats = 1

    def __enter__(self):
        print("Stopping the pumps.")
        print("Opening the doors.")

    def __exit__(self, type, value, traceback):
        # This code is guaranteed to run
        if self.boats > self.size:
            print("Sorry, you have too many boats for locke capacity.")
        else:
            print("Closing the doors.")
            print("Restarting the pumps.")
            print("Thank you for using Ballard Lockes!")

    def move_boats_through(self, boats):
        print("...boats start moving...")
        self.boats = boats

def enter_locks(num):
    small_locke = Locke(5)
    print("\n" + "1. Entering Small Locke Capacity: {},".format(small_locke.size) + " Boat Count: {}".format(num))
    print("=" * 50)
    with small_locke as locke:
        locke = small_locke.move_boats_through(num)

    large_locke = Locke(10)
    print("\n" + "2. Entering Large Locke Capacity: {},".format(large_locke.size) + " Boat Count: {}".format(num))
    print("=" * 50)
    with large_locke as locke:
        locke = large_locke.move_boats_through(num)

def main():
    enter_locks(8)


if __name__ == "__main__":
    main()
