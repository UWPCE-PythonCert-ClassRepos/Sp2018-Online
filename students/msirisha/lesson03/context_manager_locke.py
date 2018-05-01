#!/usr/bin/env python3
 """
Write a context manager class Locke to simulate the overall functioning of the system. 
When the locke is entered it stops the pumps, opens the doors, closes the doors, and restarts the pumps. 
Likewise when the locke is exited it runs through the same steps: it stops the pumps, 
opens the doors, closes the doors, and restarts the pumps. Don’t worry for now that in the
 real world there are both upstream and downstream doors, and that they should never be 
 opened at the same time; perhaps you’ll get to that later. During initialization the context manger 
 class accepts the locke’s capacity in number of boats. If someone tries to move too many boats through the locke, 
 anything over its established capacity, raise a suitable error. Since this is a simulation you need do 
 nothing more than print what is happening with the doors and pumps, like this:
"""


class Locke(object):
    """
    Simulating the overall functionality of context manager
    """
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be greater than zero")
        self.capacity = capacity

    def __enter__(self):
        """
        When the locke is entered it the stops the pupms, opens the doors, closes the doors, restarts the pumps
        """
        print("In __enter__")
        print("Stopping the pumps")
        print("Opening the doors")
        print("Closing the doors")
        print("Restarting the pumps")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        When the locke is entered it the stops the pupms, opens the doors, closes the doors, restarts the pumps
        exc_type, exc_val, exc_tb handle the exceptions.
        """
        print("In __exit__")
        print("Stopping the pumps")
        print("Opening the doors")
        print("Closing the doors")
        print("Restarting the pumps")

    def move_boats_through(self, boats):
        if boats > self.capacity:
            raise ValueError("Too many boats for locke")
        elif boats < 1:
            raise ValueError("At least one boat should be passed")
        print("Moving {} boats through".format(boats))


if __name__ == '__main__':

    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    with large_locke as locke:
        locke.move_boats_through(boats)

    with small_locke as locke:
        locke.move_boats_through(boats)
