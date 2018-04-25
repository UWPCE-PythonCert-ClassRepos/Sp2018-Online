#!/usr/bin/env python3
#
# Context Managers: Locke
# Chay Casso, 4/22/18

class Locke():

    def __init__(self, capacity):
        self.capacity = capacity

    def __enter__(self):
        return self.capacity

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