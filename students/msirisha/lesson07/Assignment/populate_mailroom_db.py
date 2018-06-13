"""
Populate db for mailroom
"""

from peewee import *
from create_mailroom_db import Donor, Donation
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


database = SqliteDatabase('./mailroom.db')

def populate_db():
    """
    """

    donor_data = [
        ("sai emani", [20.23, 30.456, 50.786]),
        ("sirisha marthy", [67.89, 45.89]),
        ("ani emani", [12.789, 5.456]),
        ("charles dickens", [15.89, 89.20, 345.67]),
        ("mark twain", [678.986]),
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for d in donor_data:
            # with database.transaction():
                new_donor = Donor.create(name=d[0], first=d[0].split()[0], last=d[0].split()[1])
                new_donor.save()
                for amt in d[1]:
                    new_donation = Donation.create(donor=d[0], amount=amt)
                    new_donation.save()
                logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {donor_data[0]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
