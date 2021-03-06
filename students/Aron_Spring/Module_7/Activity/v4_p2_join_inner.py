"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        joinn classes
"""

from peewee import *
from src.v00_personjob_model import Person, Job, Department

import logging


def join_classes():
    """
        demonstrate how to join classes together : matches
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Job class')

    logger.info('Now resolve the join and print (INNER shows only jobs that match person)...')
    logger.info('Notice how we use a query variable in this case')
    logger.info('We select the classes we need, and we join Person to Job')
    logger.info('Inner join (which is the default) shows only records that match')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job, Department)
                 .join(Job)
                 .switch(Person)
                 .join(Department)
                )

        logger.info('View matching records from both tables')
        for person in query:
            logger.info(f'Person {person.person_name} had job {person.job.job_name} in the {person.department.department_name} department ')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    join_classes()
