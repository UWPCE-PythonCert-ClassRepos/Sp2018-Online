class Locke():

	def __init__(self, capacity):
		if capacity < 1:
			raise ValueError('Capacity must be greater than zero')
		self._capacity_ = capacity


	def move_boats_through(self, number):
		if number > self._capacity_:
			raise ValueError("Number of boat exceeds locke capacity {}".format(self._capacity_))
		elif number < 1:
			raise ValueError('Boat number must be greater than zero')


	def __enter__(self):
		print("Stopping the pumps.")
		print("Opening the doors.")
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("Closing the doors.")
		print("Restarting the pumps.")
		if exc_type is not None:
			print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
		return True

if __name__ == "__main__":
	print('Here')
	small_locke = Locke(5)
	large_locke = Locke(10)
	boats = 8

	# Too many boats through a small locke will raise an exception
	with small_locke as locke:
	    locke.move_boats_through(boats)

	# A lock with sufficient capacity can move boats without incident.
	with large_locke as locke:
	    locke.move_boats_through(boats)		
