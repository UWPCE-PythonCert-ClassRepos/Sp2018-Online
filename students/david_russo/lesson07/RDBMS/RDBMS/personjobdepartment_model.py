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
    job_name = CharField(primary_key = True, max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
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

class DepartmentID(Field):
    """
    This class defines a custom Department ID field. The first character
    must be a letter, and the DepartmentID must be 4 characters long. 
    """

    logger.info('A custom field for the department class.')
    logger.info('The field forces DepartmentID to be 4 characters long.')
    logger.info('The field forces DepartmentID to start with an alpha')

    def db_value(self, value):
        """
        Ensure that value has 4 characters where the first character is numeric. 
        """
        if len(value) != 4 or not value[0].isalpha():
            raise TypeError(
                "DepartmentID must be 4 characters long and start with an alpha. "
                )
        return value

class Department(BaseModel):
    """
    This class defines Department, which maintains details of the 
    departments in which a person has held a job.
    """

    logger.info('Now we define the Department class')

    logger.info('First we enter the custom DepartmentID')
    department_number = DepartmentID()

    logger.info('Now we populate departmet name, manager, job duration, and title')
    department_name = CharField(max_length = 30)
    department_manager_name = CharField(max_length = 30)
    job_duration = IntegerField()
    job_title = ForeignKeyField(Job, related_name = 'title_of_job', null = False)


database.create_tables([
        Job,
        Person,
        Department
    ])

database.close()


