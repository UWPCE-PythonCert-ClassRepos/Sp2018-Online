import logging
from peewee import *
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# logger.info('Creating Mailroom Database')
database = SqliteDatabase('../data/mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
    class Meta:
        database = database

class Donor(BaseModel):
    """
        This class defines Donor.
    """
    # logger.info('Building Donor Class')
    first_name = CharField(primary_key= True, max_length= 30)
    last_name = CharField( max_length = 30)
    city= CharField( max_length = 30)

class Donation(BaseModel):
    """
        This is the Donation class, Because we have not specified a primary key,
        peewee will automatically add an auto-incrementing integer primary
        key field named id
    """
    # logger.info('Building Donation Class')
    created_date = DateTimeField(default=datetime.datetime.now)
    amount = DecimalField(auto_round= False, max_digits=10, decimal_places=2)
    donor = ForeignKeyField(Donor,related_name='donated_by', null=False)



database.create_tables([Donor, Donation])
database.close()