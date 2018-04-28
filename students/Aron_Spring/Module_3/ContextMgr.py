##
#"Stopping the pumps."
#"Opening the doors."
#"Closing the doors."
#"Restarting the pumps."
#This is how you might interact with your Locke class.

#small_locke = Locke(5)
#large_locke = Locke(10)
#boats = 8

# Too many boats through a small locke will raise an exception
#with small_locke as locke:
#    locke.move_boats_through(boats)

# A lock with sufficient capacity can move boats without incident.
#with large_locke as locke:
#    locke.move_boats_through(boats)


class Locke(object):
    def __init__(self, boat_count):
        self.boat_count = boat_count

#entering lockes
    def __enter__(self):
        print("Opening with '__enter__' method.")
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        return self

# moving boats through, checking boat count and locke capacity
    def boats_through_locke(self, boats):
        if boats > self.boat_count:
            raise ValueError("Too many boats for the current locke.")
        print("{} boats allowed to pass through the locke.".format(boats))

#exiting the lockes - same process
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing with '__exit__' method.")
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Starting the pumps.")




