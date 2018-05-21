"""
    Add tables for Department
"""

from peewee import *
from v00_personjob_model import Person, Job, BaseModel

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Department(BaseModel):
    """
        This class defines Department, which maintains details of
        members of a department
    """

    logger.info('Specify the fields in our model, their lengths and if mandatory')
    logger.info('Must be a unique identifier for each department')

    id = CharField(primary_key = True, max_length = 4)
    name = CharField(max_length = 30)
    manager = CharField(max_length = 30)

class Job_Department(BaseModel):
    """
        Defines the link between a job and a department.
    """

    job_name = ForeignKeyField(Job, null=False)
    dept_id = ForeignKeyField(Department, null = False)


#if __name__ == '__main__':

database = SqliteDatabase('./data/personjob.db')

database.create_tables([
    Department,
    Job_Department
])

database.close()
