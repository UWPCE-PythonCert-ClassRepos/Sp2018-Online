class Locke:
    """Simulate overall functioning of the system"""

    def __init__(self, boat_capacity):
        self.boat_capacity = boat_capacity

    def move_boats_through(self, boat_count):
        if boat_count > self.boat_capacity:
            raise ValueError("Boat count exceeds Locke capacity.")

    def enter(self):
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")

    def exit(self):
        print("Stopping the pumps.")
        print("Opening the doors.")
        print("Closing the doors.") 
        print("Restarting the pumps.")
        
