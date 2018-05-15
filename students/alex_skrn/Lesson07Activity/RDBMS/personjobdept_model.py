"""
    Simple database example with Peewee ORM, sqlite and Python
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

database = SqliteDatabase('personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')


class BaseModel(Model):
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

    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    logger.info('Now the Job class with a simlar approach')
    job_name = CharField(primary_key = True, max_length = 30)
    logger.info('Dates')
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    logger.info('Number')

    salary = DecimalField(max_digits = 7, decimal_places = 2)
    logger.info('Which person had the Job')
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)


class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('An alternate Person class')
    logger.info("Note: no primary key so we're give one 'for free'")

    person_name = CharField(max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)


class DeptIdField(CharField):
    """Custom-define a field for Department table, to impose a restriction."""

    logger.info('----------------------------------------------------')
    logger.info('Create DeptIdField class to store an alphanumerical number')
    def db_value(self, value):
        """Provide a value for the database."""
        if (len(value) != 4
                or not value[0].isalpha()
                or not value[1:].isdigit()):
            raise TypeError("DeptID: 4 chars long and start with a letter")
        return value

    def python_value(self, value):
        """Define a python value for the custom field."""
        return value


class Department(BaseModel):
    """
        This class defines Department, which maintains details of Departments
        in which Jobs were held by a Person. Referenced to unique jobs.
    """

    logger.info('----------------------------------------------------')
    logger.info('Create the Department class')
    logger.info('No PK here: the relationship is many-jobs-to-one-department')
    logger.info('attr: department number by using a special class')
    dept_num = DeptIdField()

    logger.info('attr: department name')
    dept_name = CharField(max_length=30)

    logger.info('attr: department manager name')
    dept_manager_name = CharField(max_length=30)

    logger.info('attr: length of job')
    days_in_job = IntegerField()

    logger.info('attr: job held  - a ref to a unique Job in the jobs table')
    job_held = ForeignKeyField(Job, related_name='job_held', null=False)


database.create_tables([
        Job,
        Person,
        PersonNumKey,
        Department
    ])

database.close()
