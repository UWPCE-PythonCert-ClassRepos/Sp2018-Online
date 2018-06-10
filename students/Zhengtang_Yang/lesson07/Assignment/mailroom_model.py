"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('./data/mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database

class Donor(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    name = CharField(max_length = 30)
    _id_ = IntegerField(primary_key = True)
    # first = CharField(max_length = 30)
    # last = CharField(max_length = 30)

class Donation(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    # logger.info('Now the Job class with a simlar approach')
    donor = ForeignKeyField(Donor, null = False)
    amount = FloatField(null = False)


database.create_tables([
        Donor,
        Donation,
    ])

database.close()
