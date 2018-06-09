#!/usr/bin/env python3

from peewee import SqliteDatabase
from v00_setupDB import Donor, Donation
import logging
# uuid creates a unique id that does not already exist in scope
import uuid

# Global Variables
logging.basicConfig(level=logging.CRITICAL)
raw_input = [('Tony Stark', 906.04),
             ('Captain America', 4500.00),
             ('Daisy Johnson', 14.97),
             ('Melinda May', 555.02),
             ('Phil Coulson', 9999.99)
             ]
dbname = "data.db"


def loader():
    database = SqliteDatabase(dbname)

    names = 0
    donations = 1

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for entry in raw_input:
            with database.transaction():
                new_donor = Donor.create(name=entry[names])
                # new_donor.save()
                new_donation = Donation.create(gift_id=uuid.uuid4(),
                                               value=entry[donations],
                                               donated_by=entry[names],
                                               gift_num=1)
                # new_donation.save()
                logging.info('Database add successful')

    # except Exception as e:
    #     logging.info(e)

    finally:
        logging.info('database closes')
        database.close()


if __name__ == "__main__":
    loader()
