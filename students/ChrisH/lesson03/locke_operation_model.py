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
        print("enter")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        pass


if __name__ == "__main__":

    L = Locke(15)

    with L:
        print('test')




