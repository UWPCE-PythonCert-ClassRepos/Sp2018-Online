#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom using SQL
# Dev: Scott Luse
# Date: 05/20/2018
# -------------------------------------------------#

'''
mailroom_model to create SQL database
'''

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Mailroom program using SQL database')
database = SqliteDatabase('donor.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
        This class defines Donor person, which maintains details of
        name, address, town, and zip code
    """

    donor_name = CharField(primary_key = True, max_length = 30)
    home_address = CharField(max_length=40)
    town_and_zip = CharField(max_length = 40)


class Gift(BaseModel):
    """
        This class defines Gift, which maintains details of past gifts
        given by a donor, gift key will be a combo of name, date, and time
    """

    gift_key = CharField(primary_key = True, max_length = 30)
    gift_date = DateField(formats = 'YYYY-MM-DD')
    gift_amount = DecimalField(max_digits = 7, decimal_places = 2)
    donor_name = ForeignKeyField(Donor, related_name='was_given_by', null = False)


database.create_tables([
        Gift,
        Donor,
    ])

database.close()



