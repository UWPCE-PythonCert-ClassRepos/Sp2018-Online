class Locke(object):
    """
    Class that defines a Locke Object. Since a Locke is a limited resource, it is defined using a context
    manager.
    """
    def __init__(self, capacity):
        """ The capacity of a Locke is the number of boats that can pass through it """
        self.capacity = capacity

    def __enter__(self):
        """ Enter method of the lock stops the pumps, opens the doors, closes the doors and restarts the pumps"""
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """ Frees up the resources. """
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        print("Releasing Locke and freeing up the capacity")
        return

    def move_boats_through(self, boats):
        """ If the number of boats is greater than capacity, raise an exception """
        if boats > self.capacity:
            raise Exception("The number of boats that need to move through the Locke is greater than its capacity")


if __name__ == '__main__':
    small_locke = Locke(5)
    large_locke = Locke(20)

    # with small_locke as locke:
    #     locke.move_boats_through(6)

    with large_locke as locke:
        locke.move_boats_through(6)
