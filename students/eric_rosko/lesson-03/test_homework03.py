#!/usr/bin/env python3

'''
Name:       test_homework03.py
Author:     Eric Rosko
Date:       Apr 22, 2018
Python ver. 3.6.5

Usage:  py.test test_homework03.py -v
        Usage:  py.test test_homework03.py -vv # does not truncate message
'''

from homework03 import *
import pytest


def test_locke_move_boats_through_too_many_default_zero_limit():
    with pytest.raises(Exception, match=r"Too many boats"):
        Locke().move_boats_through(1)


def test_small_locke_with_too_many_boats():
    with pytest.raises(Exception, match=r"Too many boats"):
        Locke(boat_limit = 5).move_boats_through(8)


def test_large_locke_with_boat_count_lower_than_capacity():
    Locke(boat_limit = 10).move_boats_through(8)


def test_small_locke_with_too_many_boats_logger_message():
    locke = Locke(boat_limit = 5)

    with locke:
        locke.move_boats_through(8)

    expected = '''Stopping the pumps.
Opening the doors.
Closing the doors.
Restarting the pumps.
Too many boats.  No boats are allowed to pass.
Stopping the pumps.
Opening the doors.
Closing the doors.
Restarting the pumps.
'''
    assert locke.logger == expected


def test_large_locke_with_too_many_boats_logger_message():
    locke = Locke(boat_limit = 10)

    with locke:
        locke.move_boats_through(8)

    expected = '''Stopping the pumps.
Opening the doors.
Closing the doors.
Restarting the pumps.
Moving 8 boats through the locke.
Stopping the pumps.
Opening the doors.
Closing the doors.
Restarting the pumps.
'''
    assert locke.logger == expected
