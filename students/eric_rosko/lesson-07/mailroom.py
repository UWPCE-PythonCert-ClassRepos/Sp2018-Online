#!/usr/bin/env python3

'''
Author:     Eric Rosko
Lesson:     Session 7
File:       mailroom.py
Date:       May 28, 2018
Description:
    Session 7 homework

Usage:
    python3 mailroom.py
'''

import logging
from peewee import *
from operator import *
import io

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Open database')

database = SqliteDatabase('./donors.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
        This class defines Donor, who can have multiple donations.
    """
    name = CharField(primary_key = True, max_length = 30)


class Donation(BaseModel):
    """
        This class defines Donation, which belongs to a donor.
    """
    logger.info('Create Donation class')
    donor = ForeignKeyField(Donor, related_name='donor', on_delete='CASCADE')
    amount = DecimalField(max_digits = 7, decimal_places = 2,  null = True)

database.create_tables([Donor, Donation])


def add_donation():
    fullname = input("Enter name of donor:")

    try:
        logger.info("Creating Donor")
        with database.transaction():
            result = (Donor
                  .insert(name=fullname)
                  # .on_conflict('replace')
                  .execute())
            # print("result", result)
    except Exception as e:
        logger.info(f'Error creating donor')
        logger.info(e)

    amount = input("Enter donation amount:")

    try:
        logger.info("Creating Donation for donor")
        result = (Donation
              .insert(donor=fullname, amount=amount)
              # .on_conflict('replace')
              .execute())
        print("result", result)
    except Exception as e:
        logger.info(f'Error creating donation')
        logger.info(e)

    print()
    print("Current list of donations for donor:")
    for item in Donation.select().where(Donation.amount is not None):
        print("Donation of ${0} from {1}.".format(item.amount, item.donor.name))
    print()


def list_donors():
    print("\nThere are", Donor.select().where(Donor.name is not None).count(), "total donors:")
    for item in Donor.select().where(Donor.name is not None):
        print("Donor name:", item.name)
    print()


def delete_donor():
    fullname = input("Enter name of donor to delete ")

    try:
        logger.info("Deleting Donor")
        with database.transaction():
            result = (Donor
                  .delete()
                  .where(Donor.name == fullname)
                  # .on_conflict('replace')
                  .execute())
            logger.info(f'{result} donor deleted.')

    except Exception as e:
        logger.info(f'Error deleting donor')
        logger.info(e)


def print_report():
    donor_count = Donor.select().where(Donor.name is not None).count()
    donation_count = Donation.select().where(Donation.amount is not None).count()
    print("")
    print("There are", donation_count, "donations for", donor_count, "donors:")
    for item in Donation.select().where(Donation.amount is not None):
        print("Donation of ${0} from {1}.".format(item.amount, item.donor.name))
    print()


if __name__ == "__main__":
    isRunning=True

    while isRunning:
        choice = input("1.) Add donation\n"
                       "2.) Show donors\n"
                       "3.) Show report\n"
                       "4.) Delete donor\n"
                       "Choice (q to quit):" )

        if choice == 'q':
            isRunning=False
        elif choice == '1':
            add_donation()
        elif choice == '2':
            list_donors()
        elif choice == '3':
            print_report()
        elif choice == '4':
            delete_donor()
        else:
            print ("Bad input: {}\n".format(choice))
