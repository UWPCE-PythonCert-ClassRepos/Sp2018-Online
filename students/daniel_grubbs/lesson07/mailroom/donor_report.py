#!/usr/bin/env python3
"""
Create a separate program for reading from database
"""

import os
import logging
import peewee
from create_donor_model import Donor, Donation

# Setup logging for mailroom
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Logging to console for Mailroom donor_report')

logger.info('Connecting to database')
db_file = os.path.abspath('data/donormanagement.db')
donor_db = peewee.SqliteDatabase(db_file)


def create_donor_report(database):
    """
    Prints a report from the database of donor and donations to the console.
    :return: None
    """
    # name_max = 30
    #
    # rpt_title = "Donor Name" + ' ' * (name_max - 9) + "| Total Given | Num Gifts | Average Gift"
    # print(rpt_title)
    # print("-" * len(rpt_title))

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        query = (Donor
                 .select(Donor, Donation)
                 .join(Donation, peewee.JOIN.INNER)
                 )

        logger.info('tables have been joined')

        for donor in query:
            logger.info(f'\nDonor: {donor.donor_name}' + \
                        f'\nDonor city: {donor.donor_city}' + \
                        f'\nDonation amount: {donor.donation.donation_date}' + \
                        f'\nDonation amount: {donor.donation.donation_amount}')

    except Exception as e:
        logger.info(e)
    finally:
        logger.info('closing database connection')
        database.close()
        logger.info('database connection closed')


create_donor_report(donor_db)
