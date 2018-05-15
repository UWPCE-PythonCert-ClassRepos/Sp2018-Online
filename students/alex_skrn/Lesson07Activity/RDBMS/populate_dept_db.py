"""Populate the DB with department data."""

import logging
from peewee import *
from .personjobdept_model import Department


def populate_db():
    """
    add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('----------------------------------------------------')
    logger.info('Working with Department class')
    # logger.info('Note how I use constants and a list of tuples as a simple schema')
    # logger.info('Normally you probably will have prompted for this from a user')

    dept_num = 0
    dept_name = 1
    dept_manager_name = 2
    days_in_job = 3
    job_held = 4

    departments = [
        ('S002', 'Planning', 'Bruce Willis', 1, 'Analyst'),
        ('S002', 'Planning', 'Bruce Willis', 2, 'Senior analyst'),
        ('S002', 'Strategy', 'Bruce Willis', 3, 'Senior business analyst'),
        ('A001', 'Administration', 'Eric Cartman', 10, 'Admin supervisor'),
        ('A001', 'Administration', 'Eric Cartman', 15, 'Admin manager'),
    ]

    logger.info('Create Department records: iterate through a list of tuples')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_dept = Department.create(
                    dept_num=department[dept_num],
                    dept_name=department[dept_name],
                    dept_manager_name=department[dept_manager_name],
                    days_in_job=department[days_in_job],
                    job_held=department[job_held])
                new_dept.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_dept in Department:
            logger.info(f'{saved_dept.dept_num} - {saved_dept.dept_name} ' +
                        f'headed by {saved_dept.dept_manager_name}; ' +
                        f'Days job held: {saved_dept.days_in_job}, ' +
                        f'Jon Title: {saved_dept.job_held.job_name}')

    except Exception as e:
        logger.info(f'Error creating = {department[dept_num]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
