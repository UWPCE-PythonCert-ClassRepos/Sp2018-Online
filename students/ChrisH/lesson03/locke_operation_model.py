#!/usr/bin/env python3
# ----------------------------------------------------------------
# Contains a context manager class that simulates the overall
# functioning of a waterway locke system. (Convention - spelled
# locke when used as a noun. Spelled lock when verb.)
# System functions:
#   when locke entered, stops pumps, opens doors, closes doors, restarts pumps
# When initialized, accepts capacity in number of boats. Raises error
# if too many boats try to move through Locke.
# ----------------------------------------------------------------


class Locke(object):
    """
    Context Manager class that simulates functioning of a waterway locke.
    :param capacity: number of boats locke can take
    """

    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError('Capacity must be greater than zero.')
        self.capacity = capacity

    def __enter__(self):
        print("Stopping the pumps.")
        print("Opening the doors.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing the doors.")
        print("Restarting the pumps.")
        return self

    def move_boats_through(self, boats):
        if boats > self.capacity:
            raise ValueError('Too many boats for locke size.')
        elif boats < 1:
            raise ValueError('Must send at least one boat through.')
        print("Moving {} boats through.".format(boats))

if __name__ == "__main__":

    L = Locke(15)

    with L as locke_15:
        print('test')
        print(type(L))
        print(type(locke_15))
        print(bool(locke_15 == L))
        try:
            locke_15.move_boats_through(28)
        except ValueError as err:
            print(err)
            print(type(err))

    with Locke(10) as locke_10:
        print(locke_10.capacity)







