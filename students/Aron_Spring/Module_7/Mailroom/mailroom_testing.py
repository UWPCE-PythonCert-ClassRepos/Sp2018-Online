
import logging
import pytest
from Mailroom.mailroom_functions import add_donor, add_donation
from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

"""
Testing that a donor can be added to the DB
"""

def test_add(new_donor='Test', new_city='Test', new_nickname='Test'):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        Donor.create(donor_name=new_donor, donor_city=new_city, donor_nickname=new_nickname)

    finally:
        count=Donor.select().count()
        assert count == 1

        database.close()

"""
Testing for correct DB table
"""

def table_test():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        db_tables = database.get_tables()
        return(db_tables)

    finally:
        assert db_tables[0] == 'donation'

        database.close()

"""
Testing a DB query for the newly added test user
"""
def test_query():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    database = SqliteDatabase('mailroom.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        donor_test = Donor.select().where(Donor.donor_name == 'Test')
        cursor = database.execute(donor_test).fetchone()

    finally:
        print(cursor)
        assert cursor[0] == 'Test'

        database.close()