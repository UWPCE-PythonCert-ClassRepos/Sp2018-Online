"""
    This module initially populates the Mail Room OO program
"""

import logging
from peewee import *
from mailroom_OO_model import Donors, Donations


def populate_donors_db():
    """
    add person data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    donor_name = 0

    people = [
        ('John Smith', '556 Mocking Bird Lane'),
        ('Bill Wilmer', '727 Roger Plaza'),
        ('George Guy', '56 Bugger Boulevard'),
        ('Nathan Star', '2 Easy Street')
    ]

    logger.info('Populating Donor Class')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with database.transaction():
                new_donor = Donors.create(
                    donor_name=person[donor_name])
                new_donor.save()
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Donors:
            logger.info(f'{saved_person.donor_name} lives at {saved_person.donor_address}')

    except Exception as e:
        logger.info(f'Error creating = {person[donor_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def populate_donations_db():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    donation_amount = 0
    donation_donor_name = 1

    big_money = [
        ([400], 'John Smith'),
        ([8000, 10000, 3000], 'Bill Wilmer'),
        ([50], 'George Guy'),
        ([250.50, 100], 'Nathan Star')
        ]

    logger.info('Populating Donation Class')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for cash in big_money:
            with database.transaction():
                new_money = Donations.create(
                    donation_amount=cash[donation_amount],
                    donation_donor_name=cash[donation_donor_name])
                new_money.save()
                logger.info('Database add successful')

        logger.info('Reading and print all Job rows (note the value of person)...')
        for money in Donations:
            logger.info(f'{money.job_name} : {money.start_date} to {money.end_date} for {money.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {cash[donation_amount]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()
