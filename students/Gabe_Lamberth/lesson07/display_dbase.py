"""
    Display database with Persons with jobs in departments
"""
from peewee import *
from dbase_model import Person, Job, Department
from pprint import pprint

import logging


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('activity7.db')

    logger.info('Printing Person with job and department')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job, Department)
                 .join(Job, JOIN.INNER)
                 .join(Department, JOIN.INNER)
                )

        logger.info('View matching records from all tables')
        for person in query:
            pprint(f'Person {person.person_name} had job {person.job.job_name} in {person.job.department.dept_name} department')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    main()
