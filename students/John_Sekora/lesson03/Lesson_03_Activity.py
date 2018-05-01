
class Locke(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.message = "Stopping the pumps.\n" \
                       "Opening the doors.\n" \
                       "Closing the doors.\n" \
                       "Restarting the pumps."

    def __enter__(self):
        return print(self.message)

    def move_boats_through(self, num_boats):
        self.num_boats = num_boats
        if self.num_boats > self.capacity:
            raise ValueError("too many boats")

    def __exit__(self, exc_type, exc_val, exc_tb):
        return print(self.message)

