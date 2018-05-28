"""
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
        ('Al Donor1', [10.00, 20.00, 30.00, 40.00, 50.00]),
        ('Bert Donor2', [10.00]),
        ('Connie Donor3', [10.00, 10.00, 10.01]),
        ('Dennis Donor4', [10.00, 20.00, 20.00]),
        ('Egbert Donor5', [10.39, 20.21, 10.59, 4000.40]),
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
