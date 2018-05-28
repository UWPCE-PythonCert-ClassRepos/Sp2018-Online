"""
    Modified the instructors file to remove the PersonNumKey model and
    replaced with Department model
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Building the classes from the model in the database')

logger.info('Named and connected to the database.....')

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
        This class defines Donor's, which maintains details of someone
        for whom we want to research career to date.
    """
    logger.info('Creating a Donor model')
    donor_ID = IntegerField(primary_key=True)
    first_name = CharField(max_length = 30)
    last_name = CharField(max_length=30)
    state = CharField(max_length = 2)
    job_type = CharField(max_length = 40)


class Donation(BaseModel):
    """
        This class defines Donations, which maintains details of donations
         of donors from the Donor base model.
    """
    logger.info('Creating a Donation model')
    money_ID = IntegerField(primary_key=True)
    donor_ID = ForeignKeyField(Donor, related_name='donations')
    amount = DecimalField(decimal_places=2, auto_round=False)
    date = DateField(formats = 'YYYY-MM-DD')
    notes = CharField(max_length=50, null=True)


database.create_tables([Donor, Donation])

tables = database.get_tables()

for table in tables:
    logger.info(f' Table Name : {table} was created')

database.close()
