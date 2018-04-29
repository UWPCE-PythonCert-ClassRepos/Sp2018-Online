import time
class Locke():
    def __init__(self, capacity):
        self.capacity = capacity

    def __enter__(self):
        print ('boats approaching the locke')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('locke waiting on other boats')
        return self
    
    def move_boats_through(self, boats):
        if(boats <= self.capacity):
            self.print_action()
            time.sleep(2)
            self.print_action()
        else: raise Exception

    def print_action(self):
        msg = """
        Stopping the pumps \n
        Opening the doors \n
        Closing the doors \n
        Restarting the pumps \n
        """
        print(msg)

def run_locke():
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        try:
            locke.move_boats_through(boats)
        except:
            print ('over capacity')

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        try:
            locke.move_boats_through(boats)
        except:
            print ('over capacity')


if __name__ == "__main__":
    run_locke()
