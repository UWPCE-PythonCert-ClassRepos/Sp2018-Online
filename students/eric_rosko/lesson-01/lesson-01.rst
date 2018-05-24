Lesson 01 Assignment
April 10, 2018
Eric Rosko

Comprehensions


This test in test_homework01.py generates the output.  Honestly I couldn’t get muliple list comprehensions and zip to output the correct line items, or to just filter and return only a few columns.

def test_get_with_danceable_and_loudness():
    result = filterByDanceabilityAndLoudness()
    assert len(result) == 9
    print()
    for item in result:
        print(item)


Final output for Song search:
('Migos', 'Bad and Boujee (feat. Lil Uzi Vert)')
('Drake', 'Fake Love')
('Kendrick Lamar', 'HUMBLE.')
('21 Savage', 'Bank Account')
('Jax Jones', "You Don't Know Me - Radio Edit")
('Liam Payne', 'Strip That Down')
('Future', 'Mask Off')
('Zion & Lennox', 'Otra Vez (feat. J Balvin)')
('Drake', 'Passionfruit')

Iterators & Iteratables
————————————

I’ve extended the IterateMe_1 class to support the start/step/stop parameters in the constructor.  It is a class that contains its own state, so keeps track of where it left off so it can be stopped and started again and it continues where it left off.

Range gets reset every time __iter__() is called on it which returns the ‘self’ of the object.  A new class is probably instantiate every time range is called.

If I want my IterateMe_2 to class to behave like range, where you can get what feels like a brand new iterator every time __iter___ is called, I can add the method:

.. code:: python
    def __iter__(self):
        self.current = -1
        return self

This just resets the state, and doesn’t create a brand new object.  It will start over counting whenever the iter method is called and then it will behave like an iterable like range.

Range is an ‘iterable’, because ‘iterable’ refers to the class that supports iteration.  The IterateMe classes also are iterables, because they can both return an iterator and support a next() method.  It kind of sounds like “Iterable” is a broad name for a class that supports iteration, while iterator is refering to when it is behaving like an iterator due to it possession a next() method.

Generators
—————————————

I’ve put all my generator code in generator_solution.py.
