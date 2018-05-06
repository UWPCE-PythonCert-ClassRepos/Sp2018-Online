#!/usr/bin/env python3


class Locke(object):

    def __init__(self, capacity):
        self.locke_size = capacity

    def message(self):
        # Message called by entry method
        print("Stopping the pumps...\nOpening the doors...\nClosing door...\nRestarting the pumps")

    def enter_boat(self, boats):

        if boats > self.locke_size:
            raise ValueError(f'LOADING ERROR: Number of {boats} too great! Move to larger Ballard or reduce number of boats')
        elif boats < (.5 * self.locke_size):
            # If too little boats attempt to use the larger ballard
            raise ValueError(f'LOADING ERROR: Number of {boats} too little! Use smaller ballard or queue more boats')
        else:
            print(f'\nALL CLEAR: Boats may pass through the locke.\n')
            self.message()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            self.message()
        else:
            print(str(exc_type))
            return False



