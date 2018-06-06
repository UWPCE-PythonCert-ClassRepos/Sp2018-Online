"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
"""

import logging
from peewee import *
from src.v00_personjob_model import Department  # this needs to change if you set up with a diff folder arch


def populate_db():
    """
    add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')  # navigate relative path to the db

    logger.info('Working with Department class')
    logger.info('Creating department records')

    department_number = 0
    department_name = 1
    department_manager = 2

    departments = [
        ('A111', 'Asset Management', 'Dave Sanders'),
        ('B222', 'Human Resources', 'Tammy Murray'),
        ('C333', 'Payroll', 'Daddy Warbucks'),
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_department = Department.create(
                    department_number = department[department_number],
                    department_name = department[department_name],
                    deptartment_manager = department[department_manager]
                    )
                new_department.save()
                logger.info('Department has been added to the database')

        logger.info('Reading and print all department data...')
        for saved_department in Department:
            logger.info(f'{saved_department.department_name} ' + \
                        f'Manager:  {saved_department.department_manager}. ' + \
                        f'Department number:  {saved_department.department_number}')

    except Exception as e:
        logger.info(f'Error creating = {department[department_number]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
