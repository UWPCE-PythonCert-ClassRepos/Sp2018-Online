"""Simple database example with Peewee ORM, sqlite and Python.

Here we define the schema

I only added DeptIdField class and Department class compared to the
instructor-provided code and made minor lint-demanded corrections.
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

    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


class Job(BaseModel):
    """This class defines Job, which maintains details of past Jobs held by a Person."""

    logger.info('Now the Job class with a simlar approach')
    job_name = CharField(primary_key=True, max_length=30)
    logger.info('Dates')
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    logger.info('Number')

    salary = DecimalField(max_digits=7, decimal_places=2)
    logger.info('Which person had the Job')
    person_employed = ForeignKeyField(Person,
                                      related_name='was_filled_by',
                                      null=False)


class DeptIdField(CharField):
    """Custom-define a field for Department table, to impose a restriction."""

    logger.info('Create DeptIdField class to store an alphanumerical number')

    def db_value(self, value):
        """Provide a value for the database."""
        if (len(value) != 4
                or not value[0].isalpha()
                or not value[1:].isdigit()):
            raise TypeError("DeptID to be 4 chars long + start with a letter")
        return value


class Department(BaseModel):
    """This class defines Department.

    It maintains details of Departments
    in which Jobs were held by a Person. Back-referenced to unique Jobs.
    """

    logger.info('Create the Department class')
    logger.info('No PK here: a person can hold many jobs in the same Dept')
    logger.info('But the program has a safeguard against duplicate records')
    logger.info('Create attr dept_number by using a custom class')
    dept_num = DeptIdField()

    logger.info('Create attr dept_name')
    dept_name = CharField(max_length=30)

    logger.info('Create attr department_manager_name')
    dept_manager_name = CharField(max_length=30)

    logger.info('Create attr length_of_job_in_days')
    days_in_job = IntegerField()

    logger.info('Create attr job_held -  a ref to Job table')
    job_held = ForeignKeyField(Job, related_name='job_held_at', null=False)


database.create_tables([
        Job,
        Person,
        Department
    ])

database.close()
