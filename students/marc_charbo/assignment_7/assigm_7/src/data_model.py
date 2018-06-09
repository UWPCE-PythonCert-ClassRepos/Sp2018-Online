"""
schema definition for donors in mailroom program
"""

from peewee import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        who donated.
        peewee will automatically add an auto-incrementing integer primary key field named id
    """
    username = CharField(max_length = 30, unique=True)
    person_first_name = CharField(max_length = 30, null= False)
    person_last_name = CharField(max_length = 30, null= False)

class Donation(BaseModel):
    """
        This class defines Doantion, which maintains details of the donations for each person.
         peewee will automatically add an auto-incrementing integer primary key field named id
    """
    donation_date = DateField(formats = 'YYYY-MM-DD', null= False)
    donation_amount = FloatField(null= False)
    person_donated = ForeignKeyField(Person, related_name='was_donated_by', null=False)

database.create_tables([
        Person,
        Donation
    ])

database.close()