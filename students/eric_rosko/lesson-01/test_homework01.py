#!/usr/bin/env python3

'''
Name:       test_homework01.py
Author:     Eric Rosko
Date:       Apr 8, 2018
Python ver. 3.4.3
'''


from homework01 import *
import collections

def test_get_with_danceable_and_loudness():
    result = filterByDanceabilityAndLoudness()
    assert len(result) == 9
    print()
    for item in result:
        print(item)


def test_create_tuples():
    myList = list()
    for i in range(5):
        temp = ("test", i)
        myList.append(temp)


def test_tuple():
    bob = ('Bob', 30, 'male')
    # print(type(bob))  # <class 'tuple'>
    # print('Representation:', bob, end=' ')  # ('Bob', 30, 'male')
    assert bob == ('Bob', 30, 'male')
    assert type(bob) is tuple


def test_tuple_by_index():
    bob = ('Bob', 30, 'male')
    assert bob[0] == 'Bob'
    assert bob[1] == 30
    # bob[3]  IndexError: tuple index out of range

    # A namedtuple assigns names, as well as the numerical index,
    # to each member.


def test_named_tuple():
    Person = collections.namedtuple('Person', 'name age gender')

    print('Type of Person:', type(Person))

    bob = Person(name='Bob', age=30, gender='male')
    print('\nRepresentation:', bob)

    jane = Person(name='Jane', age=29, gender='female')
    print('\nField by name:', jane.name)

    print('\nFields by index:')
    for p in [bob, jane]:
        print('%s is a %d year old %s' % p)
    print('%s is a %d year old %s' % bob)
