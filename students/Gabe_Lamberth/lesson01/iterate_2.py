#!/usr/bin/env python3


class IterateMe_2:

    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        self.current += self.step
        """
        The arithmitic returned emulates the __len__ method available to 
        the range function. Rather than being a function, range 
        is actually an immutable sequence type.        
        """
        return self.current - self.step


if __name__ == "__main__":

    """
    Unlike the the Class instantiation of the iterator, the object can be looped over without 
    consuming it. 
    """

    rt = range(2, 10, 2)

    print("Range results ")
    for i in rt:
        print(i, end=' ')
    print()
    print('The rt object has not been consumed and can be looped over')
    for i in rt:
        print(i, end=' ')
    print()

    it = IterateMe_2(2, 10, 2)
    print("Testing the iterator")
    for i in it:
        print(i, end=' ')
    print()
    print('Looping over the class object "it" returns nothing as it has been consumed by the previous loop')
    print("Testing the iterator, will return nothing because the state of the object invoked the StopIteration")
    for i in it:
        print(i, end=' ')