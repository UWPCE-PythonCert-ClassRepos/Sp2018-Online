"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

from peewee import *
from src.v00_personjob_model import Person, Job, Department

import logging


def populate_db():
    """
        add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Department class')
    logger.info('Creating Department records')

    department_name = 0
    department_number = 1
    person_in_department = 2

    departments = [
        ('Accounting', 'A001', 'Andrew'),
        ('Sales', 'S001', 'Peter'),
        ('Human Resources', 'H001','Susan'),
        ('Product', 'P001','Pam'),
        ('Research', 'R001', 'Steven')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_dept = Department.create(
                    department_name = department[department_name],
                    department_number = department[department_number],
                    person_in_department = department[person_in_department])
                new_dept.save()

        logger.info('Reading and print all Department rows...')
        for job in Job:
            logger.info(f'{department.department_name} : {department.department_number} : {department.person_in_department}')

    except Exception as e:
        logger.info(f'Error creating = {department[department_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
