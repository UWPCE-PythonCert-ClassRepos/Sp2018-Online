"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from mailroom_model import Donor, Donation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
database = SqliteDatabase('./data/mailroom.db')

def populate_db():
    """
    add department data to database
    """


    donor_input = [
        ('One', 1, [10.00,11.00,12.00,13.00]),
        ('Two', 2, [14.00]),
        ('Three', 3, [15.00,16.00,17.00,18.00]),
        ('Four', 4, [19.00,20.00,21.00]),
        ('Five', 5, [22.00,23.00])
    ]

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    for donor in donor_input:
        with database.transaction():
            logger.info(donor[0])
            new_donor = Donor(name = donor[0], _id_ = donor[1])
            new_donor.save(force_insert=True)
            for temp in donor[2]:
                new_donation = Donation.create(donor = donor[1],amount = temp)
                new_donation.save()

    logger.info('database closes')
    database.close()


if __name__ == '__main__':
    populate_db()
