"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
import os
from peewee import *
from v00_personjob_model import Department


def populate_db():
    """
    add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase(os.path.abspath('data/personjob.db'))

    logger.info('Working with Department class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    dept_number = 0
    dept_name = 1
    dept_manager = 2

    departments = [
        ('A110', 'Executive', 'Michael Gregor'),
        ('B210', 'Accounting', 'Johnny Goodfella'),
        ('C310', 'Human Resources', 'Kat Robinson'),
        ('D410', 'Engineering', 'Anita Smith'),
        ('E510', 'Facilities', 'Duke Rodgers'),
    ]

    logger.info('Creating Department records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            with database.transaction():
                new_dept = Department.create(
                    dept_number=dept[dept_number],
                    dept_name=dept[dept_name],
                    dept_manager=dept[dept_manager])
                new_dept.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_dept in Department:
            logger.info(f'{saved_dept.dept_name} ' + \
                        f'is managed by {saved_dept.dept_manager}. ' + \
                        f'The department number is {saved_dept.dept_number}')

    except Exception as e:
        logger.info(f'Error creating = {dept[dept_number]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
