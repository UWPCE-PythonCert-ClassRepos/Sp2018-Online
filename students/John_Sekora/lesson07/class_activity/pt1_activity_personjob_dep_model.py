"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('CREATING A DATABASE MODEL...')

database = SqliteDatabase('personjob.db')
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

    logger.info('Creating Model: Person Class')
    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)
    logger.info('Person Class Successful: person_name, lives_in_town, nickname')


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    logger.info('Creating Model: Person Class')
    job_name = CharField(primary_key = True, max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    logger.info('Generating Foreign Key')
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)
    logger.info('Job Class Successful: job_name, start_date, end_date, salary, person_employed')


class Department(BaseModel):
    """
        This class defines Department, which maintains details of the departments
        held of a Person's Job
    """

    logger.info('Creating Model: Department Class')
    dept_number = CharField(primary_key = True, max_length = 4)
    dept_name = CharField(max_length = 30)
    dept_manager = CharField(max_length = 30)
    dept_job_duration = IntegerField()
    logger.info('Generating Foreign Key')
    dept_job = ForeignKeyField(Job, related_name='in_department', null = False)
    logger.info('Department Class Successful: dept_number, dept_name, dept_manager, dept_job_duration, dept_person')


database.create_tables([
        Job,
        Person,
        Department,
    ])

database.close()
