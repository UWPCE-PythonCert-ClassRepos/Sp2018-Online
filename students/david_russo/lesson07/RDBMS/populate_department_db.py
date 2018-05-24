"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from .personjobdepartment_model import Person, Job, Department
from datetime import datetime


def populate_db():
    """
    add person data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../personjob.db')

    logger.info('Working with Department class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    department_number = 0
    department_name = 1
    department_manager_name = 2
    job_title = 3

    departments = [
        ('D001', 'Orders', 'Michael Scott', 'Analyst'),
        ('D001', 'Orders', 'Michael Scott', 'Senior analyst'),
        ('D002', 'Procurement', 'Meredith Palmer', 'Senior business analyst'),
        ('D003', 'eCommerce', 'Stanley Hudson', 'Admin supervisor'),
        ('D003', 'eCommerce', 'Stanley Hudson', 'Admin manager'),
    ]

    def calculate_job_duration(start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        return abs((end_date - start_date).days)


    logger.info('Creating Department records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            with database.transaction():
                # find the corresponding job
                job = Job.get(Job.job_name==dept[job_title])

                job_duration = calculate_job_duration(job.start_date, job.end_date)

                new_department = Department.create(
                    department_number=dept[department_number],
                    department_name=dept[department_name],
                    department_manager_name=dept[department_manager_name],
                    job_duration=job_duration,
                    job_title=dept[job_title])
                new_department.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_department in Department:
            logger.info(f'Department {saved_department.department_number}: ' + \
                        f'The {saved_department.department_name} department has ' + \
                        f'{saved_department.department_manager_name} as a manager ' + \
                        f'and the job {saved_department.job_title} has been worked' + \
                        f'for {saved_department.job_duration} days.')
            

    except Exception as e:
        logger.info(f'Error creating = {departments[department_number]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()

