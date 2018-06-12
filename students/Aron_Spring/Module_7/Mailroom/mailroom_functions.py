"""
    Functions to select, add and delete records within the DB
"""
from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

import logging

"""
    Search for a donor name
"""

def search_mailroom(name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        query = Donor.select().where(Donor.donor_name == name)

        for donor in query:
            if name == donor.donor_name:
                logger.info(f'{donor.donor_name} lives in {donor.donor_city}')
            else:
                logger.info(f'Donor not known')

    except Exception as e:
        logger.info(f'Error: Donor not known')
        logger.info(e)

    finally:
        database.close()

"""
    Adding a donor and details to the DB
"""

def add_donor(new_donor, new_city, new_nickname):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        Donor.create(donor_name=new_donor, donor_city=new_city, donor_nickname=new_nickname)

    finally:
        database.close()

"""
    Adding a donation to an existing donor
"""

def add_donation(new_donation, donor_name, donation_date):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        Donation.create(donation_amount=new_donation, donor_name_id=donor_name, donation_date=donation_date)

    finally:
        database.close()

#def delete_donor():
    #pass

if __name__ == '__main__':
    search_mailroom()