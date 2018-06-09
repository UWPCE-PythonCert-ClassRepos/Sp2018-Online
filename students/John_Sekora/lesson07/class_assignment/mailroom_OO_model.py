"""
    Database Model for Object Oriented Mail Room
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Connecting to database...')
database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')
logger.info('Connection to database... Successful')


class BaseModel(Model):
    class Meta:
        database = database


class Donors(BaseModel):
    """
        This class defines Donor, which maintains details
        of someone who donated to The Donation Center
    """

    logger.info('Creating Model: Donor Class')
    donor_name = CharField(primary_key=True, max_length=30)
    logger.info('Donor Class Successful: donor_name')


class Donations(BaseModel):
    """
        This class defines Donation, which maintains details
        of donations to The Donation Center
    """

    logger.info('Creating Model: Donation Class')
    donation_amount = DecimalField(decimal_places=2, auto_round=False)
    donation_donor_name = ForeignKeyField(Donors, related_name='donation_was_by', null=False)
    logger.info('Donation Class Successful: donation_amount, donation_donor_name')


database.create_tables([
        Donors,
        Donations,
    ])

database.close()
