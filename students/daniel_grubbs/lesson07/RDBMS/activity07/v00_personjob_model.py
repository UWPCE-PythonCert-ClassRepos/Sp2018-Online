"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging
import os
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase(os.path.abspath('data/personjob.db'))
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')


class BaseModel(Model):
    """
    This is the base class that Person, Job, PersonNumKey, and Department will
    inherit from. This is where all the Peewee magic happens.
    """

    # Standard syntax you use with Peewee
    class Meta:
        database = database


class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('Note how we defined the class')

    logger.info('Specify the fields in our model, their lengths and if mandatory')
    logger.info('Must be a unique identifier for each person')

    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


logger.info('Department moved above Job due to NameError.')


class Department(BaseModel):
    """
    This class defines a Persons department name (30 characters), department number
    (4 characters long and starts with a number), name of department manager, and the
    duration of days the job has been held.
    """
    logger.info("creating the departments and related information")
    logger.info("Department number")
    dept_number = CharField(primary_key=True, max_length=4)
    logger.info("Department name")
    dept_name = CharField(max_length=30)
    logger.info("Department manager")
    dept_manager = CharField(max_length=30)
    logger.info("Note: link to the Person model")


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    logger.info('Now the Job class with a simlar approach')
    job_name = CharField(primary_key=True, max_length=30)
    logger.info('Dates')
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    logger.info('Number')

    salary = DecimalField(max_digits=7, decimal_places=2)
    logger.info('Which person had the Job')
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)
    logger.info('Person was in Department')
    dept_number = ForeignKeyField(Department, related_name='dept', null=False)


class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('An alternate Person class')
    logger.info("Note: no primary key so we're give one 'for free'")

    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.create_tables([
    Job,
    Person,
    PersonNumKey,
    Department
])

database.close()
