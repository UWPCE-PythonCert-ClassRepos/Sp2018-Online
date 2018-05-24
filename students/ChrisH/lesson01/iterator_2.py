#!/usr/bin/env python


class IterateMe_2(object):
    """

    """

    def __init__(self, start, stop, step=1):
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            print("borkened")
            break
        print(i)

    for i in it:
        print(i)

    print('range test')
    n = range(2, 20, 2)
    for i in n:
        if i > 10:
            print('breaked')
            break
        print(i)

    for i in n:
        print(i)