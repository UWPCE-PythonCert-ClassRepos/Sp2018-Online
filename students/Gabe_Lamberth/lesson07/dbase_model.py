"""
    Modified the instructors file to remove the PersonNumKey model and
    replaced with Department model
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Building the classes from the model in the database')

logger.info('This file define the schema ')
logger.info('Named and connect to the database.....')

database = SqliteDatabase('activity7.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    logger.info('Creating a Person model')
    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    logger.info('Creating a Job model')
    job_name = CharField(primary_key = True, max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    # References Person to job
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)


class Department(BaseModel):
    """
        This class defines a Depart that contains Person's respective job,
        which maintains details of someone for whom we want to research career to date.
    """

    logger.info('Creating a Department model')

    dept_num = CharField(primary_key = True, max_length = 4)
    dept_name = CharField(max_length = 40)
    dept_mgr_name = CharField(max_length = 30)
    days_on_job = IntegerField()
    job_name = ForeignKeyField(Job, related_name='job_in_dept', null=False)

logger.info('Creating a Department model')
database.create_tables([
        Job,
        Person,
        Department
    ])

database.close()
