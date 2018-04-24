"""
Iterator example for range with step
"""

class IterateMe_2:
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration


if __name__ == "__main__":
    print("Testing the iterator")
    it = IterateMe_2(2,20,2)
    # What happens if you break from a loop and try to pick it up again:
    for i in it:
        if i > 10:
            print("Breaking after 10")
            break
        print(i)
    # printing again
    print("Re running again IterateMe_2")
    for i in it:
        print(i)
    # It picked where it left off and skipped 12 and printed numbers 14,16, 18.

    # Will compare with range.
    print("Lets compare the behaviour with actual range function")
    range_it = range(2, 20, 2)
    for i in range_it:
        if i > 10:
            print("Breaking after 10")
            break
        print(i)
    # printing again
    print("re running range function")
    for i in range_it:
        print(i)
