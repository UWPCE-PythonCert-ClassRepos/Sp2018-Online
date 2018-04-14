#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 01 - Iterators
    SUB TITLE: Iterators vs Range
      CREATOR: PydPiper
 DATE CREATED: 4/14/18
LAST MODIFIED: 4/14/18
  DESCRIPTION: Create an iterator that mimics an iterable (like range) iterator_2(start, stop, step=1)
               The lesson learned here is that a for loop is a iter + infinite while loop:

               for i in iterable_object:

               # is the same as

               for_iterable = iter(iterable_object)
               while True:
                try:
                    next(for_iterable)
                except StopIteration
                    break

                Therefore, a for loop calls class.__iter__(), to have a iterator mimic an iterable like range,
                we simply just need to reset the iterator's state when a __iter__() is called on it. See example below

                The difference between an iterator and an iterable is that an iterator generates next values with each
                state, while a iterable is a list like collection of values that you can step through
********************************************************************************************************************"""


class Iterator_2():
    """
    Iterator class. Takes a start, stop and step (int) and via next() or .__next() the iterator returns the next state
    """

    def __init__(self, start, stop, step=1):
        """
        Iterator initializer for start, stop, step, state (internal), current (internal)
        :param start: int, never overwritten used to recall initial state
        :param stop: int, used to upper bound the iterator
        :param step: int, step size between states
        """
        self.start = start
        self.stop = stop
        self.step = step

        self.state = -1
        self.current = start

    def __iter__(self):
        """
        Enables the class object to be called by iter(object), same as, object.__inter__()
        :return: self, an iterable. Prior to return, state is reset for code recall (reinitialized)
        """
        self.state = -1
        return self

    def __next__(self):
        """
        Enables the class object to be called by next(object), same as, object.__next__()
        :return: self.start + (self.step * self.state), where self.state is incremented with each "next"
        """
        self.state += 1
        self.current = self.start + (self.step * self.state)
        if self.current < self.stop:
            return self.current

        else:
            raise StopIteration
