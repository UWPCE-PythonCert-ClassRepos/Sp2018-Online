#!/usr/bin/env python3

'''
Name:       test_mailroom.py
Author:     Eric Rosko
Date:       May 4, 2018
Python ver. 3
'''


from mailroom import *


def test_get_donor_names_mutliple_names():
    data = dict(a=[], b=[])
    assert get_donor_names(data) == 'a, b'

def test_get_donor_names_one_name():
    data = dict(a=[])
    assert get_donor_names(data) == 'a'

def test_add_donation_for_person():
    data = dict()
    assert is_person_in_database(data,'bob') == False
    add_donation_for_person(data,'bob', 5.00)
    assert is_person_in_database(data,'bob') == True

def test_add_two_donations_for_person():
    data = dict()
    add_donation_for_person(data,'bob', 5.00)
    add_donation_for_person(data,'bob', 6.00)
    t = data['bob']

    assert sum(t) == 11

def test_person_not_in_database():
    data = dict(bob=[1.01])
    assert is_person_in_database(data,'bob') == True

def test_person_not_in_database():
    data = dict(bob=[1.01])
    assert is_person_in_database(data,'ann') == False

def test_verify_number_with_int():
    assert verify_number(5) == True

def test_verify_number_with_float():
    assert verify_number(5.5) == True

def test_verify_number_with_text():
    assert verify_number('hi') == False

def test_print_database():
    data = dict(one=[1.01], two=[2.01,2.02], three=[3.01,3.02,3.03], four=[.5])
    assert print_report(data) == "Donor:three\tTotal:9.06\tCount:3\t\tAverage:3.02\nDonor:two\tTotal:4.03\tCount:2\t\tAverage:2.01\nDonor:one\tTotal:1.01\tCount:1\t\tAverage:1.01\nDonor:four\tTotal:0.50\tCount:1\t\tAverage:0.50\n"

def test_dictionary_add():
    donators = {}
    donators['one']=['1.00']
    assert len(donators) == 1
    atuple = donators.popitem()
    assert atuple[1][0] == '1.00'

def test_dictionary_length():
    donators = dict(one=[1.00])
    assert len(donators) == 1


if __name__ == "__main__":
    pass
