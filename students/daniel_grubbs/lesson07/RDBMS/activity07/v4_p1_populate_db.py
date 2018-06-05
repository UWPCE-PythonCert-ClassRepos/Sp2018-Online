"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
import os
from peewee import *
from v00_personjob_model import Person, Job


def populate_db():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase(os.path.abspath('data/personjob.db'))

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    job_name = 0
    start_date = 1
    end_date = 2
    salary = 3
    person_employed = 4
    dept_number = 5

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew', 'A110'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew', 'B210'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew', 'C310'),
        ('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter', 'D410'),
        ('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter', 'E510')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name=job[job_name],
                    start_date=job[start_date],
                    end_date=job[end_date],
                    salary=job[salary],
                    person_employed=job[person_employed],
                    dept_number=job[dept_number])
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed} + \
                        {job.dept_number}')

    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
