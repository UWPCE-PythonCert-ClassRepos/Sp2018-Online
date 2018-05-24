"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from .donor_donation_model import Donation


def populate_db():
    """
    add donor data to database
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Working with Donation class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    database = SqliteDatabase('donor_donation.db')
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

    DONATION_AMOUNT = 0
    DONOR_NAME = 1
    

    donations = [
        (500.01, 'Bobby Wagner'),
        (700.01, 'Earl Thomas'),
        (900.01, 'Chris Carson'),
        (1100.01, 'Bobby Wagner'),
        (1300.01, 'Earl Thomas'),
        (1500.01, 'Chris Carson'),
        ]

    logger.info('Creating Donations records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to rollback on error')

    for donation in donations:
        try:
            with database.transaction():
                new_donation = Donation.create(
                        donation_amount = donation[DONATION_AMOUNT],
                        donor_name = donation[DONOR_NAME])
                new_donation.save()
                logger.info('Database add successful')

        except Exception as e:
            logger.info(f'Error creating = {donation[DONOR_NAME]}')
            logger.info(e)
            logger.info('See how the database protects our data')

    logger.info('Read and print all Donor records we created...')

    for donation in donations:
        logger.info(f'Donor Name: {donation[DONOR_NAME]}' + \
                    f'Donor Amount: {donation[DONATION_AMOUNT]}')

    database.close()


if __name__ == '__main__':
    populate_db()

