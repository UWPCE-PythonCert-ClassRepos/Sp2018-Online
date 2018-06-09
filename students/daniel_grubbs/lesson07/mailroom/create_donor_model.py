#!/usr/bin/env python3
"""
Use Peewee to model the data for the Mailroom program.

Show logging messages as the different items are created.
"""
import peewee
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db_file = os.path.abspath('data/donormanagement.db')
donor_db = peewee.SqliteDatabase(db_file)
donor_db.connect()
donor_db.execute_sql('PRAGMA foreign_keys = ON;')


# Standard definition for our BaseModel class
class BaseModel(peewee.Model):
    class Meta:
        logger.info('need to use database as the variable. Setup for use with donor_db')
        database = donor_db


# Below we will create two classes that define our tables
logger.info("creating the Donor table for the database.")


class Donor(BaseModel):
    """This class defines Donor, which maintains details
     about the Donor."""

    donor_name = peewee.CharField(primary_key=True, max_length=30)
    logger.info('donor_name created')
    donor_city = peewee.CharField(max_length=30)
    logger.info('donor_city created')


logger.info("creating the Donation table for the database.")
logger.info("using donor_name for the ForeignKeyField")


class Donation(BaseModel):
    """This class defines a donor's donations."""
    # donation_id = peewee.CharField(primary_key=True, max_length=30)
    donation_amount = peewee.DecimalField(max_digits=10, decimal_places=2)
    logger.info('donation_amount created')
    donor_name = peewee.ForeignKeyField(Donor, related_name='was_donated_by', null=False)
    logger.info('donor_name ForeignKeyField created')

    # The donation_date field may not be used but
    # is something that would be good for record keeping
    # so adding it in case Mailroom needs to be made
    # more robust in the future.
    donation_date = peewee.DateField(formats='YYYY-MM-DD')
    logger.info('donation_date created')


donor_db.create_tables([
    Donation,
    Donor,
])
logger.info('database tables created')

donor_db.close()
logger.info('database closed')
