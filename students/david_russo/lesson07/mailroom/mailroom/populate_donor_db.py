"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from .donor_donation_model import Donor


def populate_db():
    """
    add donor data to database
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Working with Donor class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    database = SqliteDatabase('donor_donation.db')
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

    DONOR_NAME = 0
    DONOR_OCCUPATION = 1
    

    donors = [
        ('Bobby Wagner', 'NFL player'),
        ('Earl Thomas', 'NFL player'),
        ('Chris Carson', 'NFL player'),
        ]

    logger.info('Creating Donor records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to rollback on error')

    for donor in donors:
        try:
            with database.transaction():
                new_donor = Donor.create(
                        donor_name = donor[DONOR_NAME],
                        donor_occupation = donor[DONOR_OCCUPATION])
                new_donor.save()
                logger.info('Database add successful')

        except Exception as e:
            logger.info(f'Error creating = {donor[DONOR_NAME]}')
            logger.info(e)
            logger.info('See how the database protects our data')

    logger.info('Read and print all Donor records we created...')

    for donor in donors:
        logger.info(f'Donor Name: {donor[DONOR_NAME]}' + \
                    f'Donor Occupation: {donor[DONOR_OCCUPATION]}')

    database.close()


if __name__ == '__main__':
    populate_db()

