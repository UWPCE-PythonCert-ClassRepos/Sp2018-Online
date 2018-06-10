"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from v00_personjob_model import Department


def populate_db():
    """
    add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    department_number = 0
    department_name = 1
    department_manager = 2

    departments = [
        ('A101', 'US', 'Donald'),
        ('A201', 'China', 'Xi'),
        ('A301', 'Russia', 'Putin'),
        ('A401', 'Germany', 'Merkel'),
        ('A501', 'Canada', 'Trudeau'),
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_department = Department.create(
                    department_number = department[department_number],
                    department_name = department[department_name],
                    department_manager = department[department_manager])
                new_department.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_department in Department:
            logger.info(f'Dept_num:{saved_department.department_number} Name:{saved_department.department_name} ' + \
                        f'Manager {saved_department.department_manager}')

    except Exception as e:
        logger.info(f'Error creating = {department[department_name]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
