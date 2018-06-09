"""
    Simple database examle with Peewee ORM, sqlite and Python
    Here we define the schema

"""

from peewee import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('act7.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
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

class Department(BaseModel):
    """
        This class defines Department, which maintains details department a Person held a Job.
    """
    logger.info('A Department class')
    logger.info("Must be a unique identifier for each Department, which is the department number")
    department_number = CharField(primary_key = True,max_length=4)
    department_name = CharField(max_length = 30)
    department_manager = CharField(max_length=30)
    days_on_job = IntegerField()
    job_title = ForeignKeyField(Job, related_name='job_department', null=False)

database.create_tables([
        Job,
        Person,
        Department
    ])

database.close()