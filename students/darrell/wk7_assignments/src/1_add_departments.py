"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

from peewee import *
from create_db import Person, Job, Department

import logging


def populate_db():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    department_number = 0
    department_name = 1
    department_manager = 2
    person_in_department_id = 3

    departments = [
        ('a0001', 'Sales', 'Mgr Bob'),
        ('a0002', 'Finance', 'Scrouge'),
        ('a0003', 'Engineering', "Bill Gates")
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            with database.transaction():
                new_dept = Department.create(
                    department_number = dept[department_number],
                    department_name = dept[department_name],
                    department_manager = dept[department_manager])
                new_dept.save()

        logger.info('Reading and print all Department rows (note the value of person)...')
        for dept in Department:
            logger.info(f'{dept.department_number} : {dept.department_name}  managed by {dept.department_manager}')

    except Exception as e:
        logger.info(f'Error creating = {dept[department_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
