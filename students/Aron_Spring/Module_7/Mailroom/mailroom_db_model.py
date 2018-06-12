"""
    Donor and donation details using  Peewee ORM amd sqlite
    Here is the basic DB schema and logging info
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')


class BaseModel(Model):
    """
    Baseclass for the DB classes to be used
    """

    class Meta:
        database = database


class Donor(BaseModel):
    """
    The Donor class, which includes donor specifics for tracking.
    Details including name, city and if there is a nickname

    """
    logger.info('Name is a unique identifier for each entry')

    donor_name = CharField(primary_key=True, max_length=30)
    donor_city = CharField(max_length=40)
    donor_nickname = CharField(max_length=20, null = True)


class Donation(BaseModel):
    """
    The donation class, all info about donations including
    amount and date. Primary key assigned automatically
    """

    logger.info('Creation of the donation table')

    donation_amount = DecimalField(max_digits=7, decimal_places=2)
    donor_name = ForeignKeyField(Donor, related_name='donor', null=False)
    donation_date = DateField(formats = 'YYYY-MM-DD')


database.create_tables([
    Donor,
    Donation
])

database.close()