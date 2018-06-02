#!/usr/bin/env python3

'''
Name:       test_mailroom.py
Author:     Eric Rosko
Date:       May 28, 2018
Assignment: 7
Python ver. 3

Usage: py.test -sv

'''

import logging
import pytest
from mailroom import logger
from peewee import *
from mailroom import Donor, Donation
# from mailroom import database


def setup_function(function):
    """
    Runs once before each function in this file.
    """
    # global database
    database = SqliteDatabase('donors.db')
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only
    # database.create_tables([ Donor, Donation])
    # database.execute_sql("delete from Donor")
    # database.execute_sql("delete from Donation")


def teardown_function(function):
    # global database
    database.close()


def test_add_donor():
    global database
    try:
        with database.transaction():
            new_donor = Donor.create(
                        name = 'Bob3')
            new_donor.save()

        logger.info('Reading and print donor')
        for donor in Donor:
            logger.info(f'{donor.name}')

    except Exception as e:
        logger.info(f'Error creating donor')
        logger.info(e)

    # with database.transaction():
    count = Donor.select().count()
    print("count is", count)
    assert count == 1


def test_add_two_donors():
    global database
    try:
        with database.transaction():
            new_donor = Donor.create(
                        name = 'Bob')
            new_donor.save()

            new_donor2 = Donor.create(
            name = 'Dave')
            new_donor2.save()

        logger.info('Reading and print donor')
        for donor in Donor:
            logger.info(f'{donor.name}')

    except Exception as e:
        logger.info(f'Error creating donor')
        logger.info(e)

    # with database.transaction():
    count = Donor.select().count()
    print("count is", count)
    assert count == 2


def test_add_donation():

    try:
        with database.transaction():
            new_donor = Donor.create(
                        name = 'Bob')
            new_donor.save()

        with database.transaction():
            new_donation = Donation.create(donor_id=new_donor.name,
                                            amount=123.45)
            new_donation.save()

    except Exception as e:
        logger.info(f'Error creating donation')
        logger.info(e)


if __name__ == "__main__":
    pass
