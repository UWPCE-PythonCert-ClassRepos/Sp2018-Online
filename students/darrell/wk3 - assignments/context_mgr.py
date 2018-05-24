from contextlib import contextmanager


class Locke():

    def __init__(self, capacity):
        self.capacity = capacity



    def __enter__(self):
        return self


    def move_boats_through(self, number_of_boats):
        if number_of_boats > self.capacity:
            raise Exception('error, not enough capacity')
        else:
            print("Stopping the pumps.\nblah blah")


    def __exit__(self, e_type, e_val, e_traceback): # or *args
        print(e_val)
        print('sweeping the deck and cleaning up resources')


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

# Too many boats through a small locke will raise an exception
with small_locke as locke:
    locke.move_boats_through(boats)

# # A lock with sufficient capacity can move boats without incident.
# with large_locke as locke:
#     locke.move_boats_through(boats)