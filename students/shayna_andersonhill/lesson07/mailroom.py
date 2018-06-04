#!/usr/bin/env python
"""
This is an object oriented version
"""

import sys
import os
import logging
import math
from textwrap import dedent
from peewee import SqliteDatabase, Model, CharField, UUIDField, ForeignKeyField, DecimalField, SQL
import uuid
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

database = SqliteDatabase('mailroom.db')

database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    donor_id = UUIDField(primary_key=True)
    donor_name = CharField(max_length=30)
#    donor_address = CharField(max_length = 100)

    @staticmethod
    def get_donors_and_donations():
        donor_and_donations = {}
        for donor in Donor.select():
            donor_and_donations.update({donor.donor_name: get_donations(donor.donor_id)})
        return donor_and_donations


class Donations(BaseModel):
    donor_id = ForeignKeyField(Donor, field='donor_id', null=False)
    donation = DecimalField(max_digits=10, decimal_places=2)
#    donation_date = DateField(formats = 'YYYY-MM-DD')

    @staticmethod
    def get_donations(donor_id):
        values = []
        donations = Donations.select().where(donor_id == donor_id)
        for donation in donations:
            values.append(float(donation.donation))

        return values


# Utility so we have data to test with, etc.
def populate_db():
    """
    returns a list of donor objects to use as sample data


    """
    database.create_tables([
        Donor,
        Donations
    ])

    database.close()

    donors = ["William Gates III",
              "Jeff Bezos",
              "Paul Allen",
              "Mark Zuckerberg"]

    for donor in donors:
        with database.transaction():
            donor_id = create_donor(name=donor)
            donation = random.randint(0, 10000)
            create_donation(amount=donation, donor_id=donor_id)
            logger.info(f"Added {donor} to the database with a donation of ${donation}")


def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    action = input(dedent('''
      Choose an action:

      1 - Send a Thank You
      2 - Create a Report
      3 - Quit

      > '''))
    return action.strip()


def send_thank_you():
    """
    Record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            try:
                for donor in Donor.select():
                    print(donor.donor_name)
            except Exception as e:
                logger.error("Error get donar list")
                logger.error(e)
                raise

        elif name == "menu":
            return
        else:
            break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            # extra check here -- unlikely that someone will type "NaN", but
            # it IS possible, and it is a valid floating point number:
            # http://en.wikipedia.org/wiki/NaN
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        # in this case, the ValueError could be raised by the float() call, or by the NaN-check
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    # If this is a new user, ensure that the database has the necessary
    # data structure.
    try:
        donor_id = None
        donor = database.execute_sql(f"select * from Donor where donor_name == '{name}';").fetchone()

        if donor is None:
            with database.transaction():
                donor_id = create_donor(name)

        # Record the donation
        with database.transaction():
            _id = donor[0] if not donor_id else donor_id
            create_donation(amount, _id)

        logger.info(f"Added {name} to the database with a donation of ${amount}")
        print(f"""
        Thanks for you donation of {amount}.
        Now go jump in a lake {name}""")

    except Exception as e:
        logger.error(e)
        raise
    finally:
        database.close()


def create_donation(amount, donor_id):
    new_donation = Donations.create(
        donor_id=donor_id,
        donation=amount
    )
    new_donation.save()


def create_donor(name):
    donor_id = uuid.uuid4()
    new_donor = Donor.create(
        donor_id=donor_id,
        donor_name=name
    )
    new_donor.save()
    return donor_id


def print_donor_report():
    print(Donor.get_donors_and_donations())


def quit():
    sys.exit(0)


def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    populate_db()
    main()
