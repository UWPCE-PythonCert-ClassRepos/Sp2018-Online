#!/usr/bin/env python3
"""Context manager for lesson 3 Locke assignment. """


class Locke(object):
    def __init__(self, capacity):
        self.capacity = capacity

        def __enter__(self):
            'Enter the Locke -  stop the pumps, open the doors and then close the doors and re-start the pumps'
            print("ENTER")
            print("Stopping the pumps")
            print("Opening the doors")
            print("Closing the doors")
            print("Restarting the pumps")

        def __exit__(self, type, value, traceback):
            'Exit the Locke - stop the pumps, open the doors and then close the doors and re-start the pumps'
            print("EXIT")
            print("Stopping the pumps")
            print("Opening the doors")
            print("Closing the doors")
            print("Restarting the pumps")

        def move_boats_through(self, boats):
            ' Too many boats through a small locke will raise an exception'
            if boats > self.capacity:
                raise ValueError("Too many boats for locke")
            elif boats < 1:
                raise ValueError("No boats are detected")
            print("Moving {} boats through".format(boats))


if __name__ == '__main__':
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8
