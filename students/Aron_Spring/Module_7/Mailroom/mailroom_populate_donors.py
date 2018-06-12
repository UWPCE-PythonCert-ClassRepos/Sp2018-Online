"""
Populating DB with initial donor and donation info
"""

from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

import logging

def populate_donors():

    """
        add donor and donation data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    logger.info('Creating Donor records')

    donor_name = 0
    donor_city = 1
    donor_nickname = 2

    donors = [
        ('Bob', 'Seattle', 'Bobby'),
        ('Joan', 'Ballard', 'Null')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donors:
            with database.transaction():
                new_donor = Donor.create(
                    donor_name = donor[donor_name],
                    donor_city = donor[donor_city],
                    donor_nickname = donor[donor_nickname])
                new_donor.save()

    finally:
        database.close()

if __name__ == '__main__':
    populate_donors()