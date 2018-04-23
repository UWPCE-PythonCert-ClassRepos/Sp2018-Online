#!/usr/bin/env python3

'''
Name:       homework03.py
Author:     Eric Rosko
Date:       Apr 22, 2018
Python ver. 3.6.5
'''

class Locke:
    def __init__(self, boat_limit=0):
        self.boat_limit = boat_limit
        self.logger = ""


    def move_boats_through(self, boat_count):
        if boat_count > self.boat_limit:
            output = "Too many boats.  No boats are allowed to pass."
            self.logger += output + '\n'
            print(output)
            raise Exception("Too many boats")

        boat_wording = "1 boat" if boat_count == 1 else "{0} boats".format(boat_count)
        output = "Moving " + boat_wording + " through the locke."
        self.logger += output + '\n'


    def __enter__(self):
        output = "Stopping the pumps.\nOpening the doors.\nClosing the doors.\nRestarting the pumps."
        self.logger += output + '\n'
        print(output)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        output = "Stopping the pumps.\nOpening the doors.\nClosing the doors.\nRestarting the pumps."
        self.logger += output + '\n'
        print(output)
        return self


if __name__ == "__main__":
    pass
