"""Class defined for locke function. Initialize the capacity when creating an instance. Then use context manager with "with" to get the output from the methods. Raise ValueError exception if the boats are higher than the capacity"""
class locke():
    def __init__(self, capacity):
        self.capacity = capacity
        self.boats = 1

    def __enter__(self):
        print("Stopping the pumps \nOpening the doors \nClosing the doors \nRestarting the pumps")
        return self

    def move_boats_through(self, no_of_boats):
        if no_of_boats <= self.capacity:
            print("Moving the boats")
        else:
            raise ValueError("Reached Capacity of {}".format(self.capacity))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting \nStopping the pumps \nOpening the doors \nClosing the doors \nRestarting the pumps")


small_locke = locke(5)
large_locke = locke(10)
boats = 8

with small_locke as locke:
    locke.move_boats_through(boats)

with large_locke as locke:
    locke.move_boats_through(boats)
