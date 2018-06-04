"""
    Functions to select, add and delete records within the DB
"""
from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

import logging

def search_mailroom():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')
    Donor.get(donor.donor_name == 'Joan')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        #logger.info('Find and display by selecting a specific Donor')
        #aperson = Donor.get(Donor.donor_name == 'Joan')
        query = (Donor
                 .select(Donor.donor_name=='Joan'))

    for person in query:
        logger.info(f'{Donor.donor_name} lives in {Donor.donor_city}')

    finally:
        database.close()
"""
#def add_donor():
    #pass

#def add_donation():
    #pass

#def delete_donor():
    #pass

if __name__ == '__main__':
    search_mailroom()

query
Out[32]: <Mailroom.mailroom_db_model.Donor at 0x2229a8c9da0>
query = Donor.select().where(Donor.donor_name == 'Joan')
cursor = database.execute(query)
print(cursor.fetchone())
('Joan', 'Ballard', 'Null')
database
Out[36]: <peewee.SqliteDatabase at 0x2229a8c98d0>