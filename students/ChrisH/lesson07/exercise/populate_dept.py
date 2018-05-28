"""
    Populate department table with data
"""

from peewee import *
# from v00_personjob_model import Person, Job
from add_dept import Department, Job_Department


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('./data/personjob.db')

def populate_department():
    """
        add job data to database
    """
    logger.info('Working with Department class')
    logger.info('Creating Department records')

    dept_id = 0
    name = 1
    manager = 2

    depts = [
        ('A123', 'Sales', 'Nod Doff'),
        ('B777', 'Marketing', 'Al Geddit'),
        ('C458', 'Information Technology', 'Ivan Hassanich')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in depts:
            with database.transaction():
                new_dept = Department.create(
                    id = dept[dept_id],
                    name = dept[name],
                    manager = dept[manager])
                new_dept.save()

        logger.info('Reading and print all Department rows...')
        for dept in Department:
            logger.info(f'{dept.id} : {dept.name} managed by {dept.manager}')

    except Exception as e:
        logger.info(f'Error creating = {dept[dept_id]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def populate_job_department():

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        cross = [('Analyst', 'C458'),
                 ('Senior analyst', 'C458'),
                 ('Senior business analyst', 'A123'),
                 ('Admin supervisor', 'B777'),
                 ('Admin manager', 'A123')]

        for c in cross:
            with database.transaction():
                new_cross = Job_Department.create(
                    job_name = c[0],
                    dept_id = c[1]
                )
                new_cross.save()

        logger.info('Reading and print all Job/Dept Cross reference rows...')
        for c in Job_Department:
            logger.info(f'Job: {c.job_name} is in department: {c.dept_id}')

    except Exception as e:
        logger.info(f'Error creating = {c[0]}:{c[1]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_department()
    populate_job_department()
