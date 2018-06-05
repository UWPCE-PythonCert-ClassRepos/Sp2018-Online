"""
    Donor and donations with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging 
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase('donor_donation.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')

class BaseModel(Model):
	"""
	This baseclass defines a convenient template from which we can 
	build models.
	"""
	class Meta:
		database = database

class Donor(BaseModel):
	"""
	This class defines Donor, which maintains details about the specific
	donor. We will omit donation summaries such as total donation amount
	and number of donations, and let peewee do that work for us in the
	report creation.
	"""
	donor_name = CharField(primary_key=True, max_length=30)
	donor_occupation = CharField(max_length=30)

class Donation(BaseModel):
	"""
	This class defines Donations, which maintains information
	such as donation amount and donating party 
	"""
   
	donation_amount = DecimalField(max_digits=5, decimal_places=2)
	donor_name = ForeignKeyField(Donor, related_name = 'donator', null = False)


database.create_tables([
        Donor,
        Donation
    ])

database.close()

