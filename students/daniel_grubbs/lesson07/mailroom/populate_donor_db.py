#!/usr/bin/env python3
"""
Populate the Donor database with data
"""
import logging
import peewee
from create_donor_model import Donor, Donation


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = peewee.SqliteDatabase('data/donormanagement.db')

def populate_db_donor():
    """
    add donor to the database
    """
    logger.info('Populating donors into the database')

    donor_name = 0
    donor_city = 1

    donors = [
        ('Jimmy Nguyen', 'Houston'),
        ('Steve Smith', 'Seattle'),
        ('Julia Norton', 'Portland'),
        ('Ed Johnson', 'Atlanta'),
        ('Elizabeth McBath', 'Austin')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donors:
            with database.transaction():
                new_donor = Donor.create(
                    donor_name=donor[donor_name],
                    donor_city=donor[donor_city])
                new_donor.save()
                logger.info('Database add successful')

        for saved_donor in Donor:
            logger.info(f'{saved_donor.donor_name} is in database.')

    except Exception as e:
        logger.info('Error creating = {donor[DONOR_NAME}')
        logger.info(e)
        logger.info('Database protected our data')

    finally:
        logger.info('database closes')
        database.close()


def populate_db_donation():
    """
    add donation to the database
    """
    logger.info('Opening connection to the database')

    logger.info('Adding donations in for the populated donors.')
    donation_amount = 0
    donation_date = 1
    donor_name = 2

    donations = [
        (3772.32, '2018-05-23',  'Jimmy Nguyen'),
        (877.33, '2018-05-22', 'Steve Smith'),
        (663.23, '2018-05-21', 'Julia Norton'),
        (1663.23, '2018-05-20', 'Ed Johnson'),
        (2200.23, '2018-05-19', 'Elizabeth McBath')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                    donation_amount=donation[donation_amount],
                    donation_date=donation[donation_date],
                    donor_name=donation[donor_name])
                new_donation.save()
                logger.info('Database add successful')

        for saved_donation in Donation:
            logger.info(f'{saved_donation.donor_name} pledged {saved_donation.donation_amount}.')

    except Exception as e:
        logger.info('Error creating = {donation[donor_name}')
        logger.info(e)
        logger.info('Database protected our data')

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db_donor()
    populate_db_donation()
