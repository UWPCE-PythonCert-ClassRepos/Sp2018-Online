#!/usr/bin/env python3
#
# Context Managers: Locke
# Chay Casso, 4/22/18

# Sorry, I can't get this to work. But I'm not sure what exactly is wrong with this.
# I get a __enter__ attribute error.
# But this is what I feel like this should look like.

class Locke():

    def __init__(self, capacity):
        self.capacity = capacity

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")

    def move_boats_through(self, boats):
        self.boats = boats
        if self.boats < self.capacity:
            print("Stopping the pumps.")
            print("Opening the doors.")
            print("Closing the doors.")
            print("Restarting the pumps.")
        else:
            raise Exception("Capacity not sufficient for number of boats.")
