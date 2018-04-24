#!/usr/bin/env python

class Locke():

	# initialize the objects
	def __init__(self, boat_capacity):
		self.boat_capacity = boat_capacity

	# method to move boats through the locks
	def move_boats_through(self, number_of_boats):
		self.number_of_boats = number_of_boats
		if self.number_of_boats > self.boat_capacity:
			raise ValueError("The locke cannot handle more than {} boats. ".format(self.boat_capacity))


	# necessary method to enter the locks
	def __enter__(self):
		print("Stopping the pumps. ")
		print("Opening the doors. ")
		return self

	# necessary method to exit the locks
	def __exit__(self, type, value, traceback):
		print("Closing the doors. ")
		print("Restarting the pumps. ")

