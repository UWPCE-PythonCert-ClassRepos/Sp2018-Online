"""
Populating DB with initial donor and donation info
"""

from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

import logging

def populate_donations():

    """
        add donor and donation data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    logger.info('Creating Donor and Donation records')

    donation_amount = 0
    donor_name = 1
    donation_date = 2

    donations = [
        ('100.00', 'Bob', '2018-04-24'),
        ('1000.00', 'Joan', '2018-03-12')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                    donation_amount = donation[donation_amount],
                    donor_name = donation[donor_name],
                    donation_date = donation[donation_date])
                new_donation.save()

    finally:
        database.close()

if __name__ == '__main__':
    populate_donations()