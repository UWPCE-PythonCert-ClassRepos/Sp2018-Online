#!/usr/bin/env python3

"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

from peewee import *
from v00_personjob_model import Person, Job, Department
from datetime import datetime
import logging

def populate_departments():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    logger.info('Working with Department class')
    logger.info('Creating Department records')

    dept_number = 0
    dept_name = 1
    start_date = 2
    end_date = 3

    departments = [
        ('A001', 'Mailroom', '2001-09-22', '2003-01-30'),
        ('B001', 'Sales', '2003-02-01', '2006-10-22')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        # delete the departments since they are added each time
        # this script is run.
        # d1 = Department.get(Department.name == 'Mailroom')
        # d1.delete_instance()
        # d2 = Department.get(Department.name == 'Sales')
        # d2.delete_instance()

        for department in departments:
            with database.transaction():
                logger = logging.getLogger(f'creating {department[dept_name]}')
                new_dept = Department.create(
                    number = department[dept_number],
                    name = department[dept_name],
                    start_date = department[start_date],
                    end_date = department[end_date])
                new_dept.save()

        logger.info('Reading and print all Department rows...')
        for dept in Department:
            logger.info(f'{dept.number} {dept.name}: {dept.start_date} to {dept.end_date}')

    except Exception as e:
        logger.info(f'Error creating = {department[dept_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

def populate_jobs():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    job_name = 0
    start_date = 1
    end_date = 2
    salary = 3
    person_employed = 4
    department_number = 5

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew', 'A001'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew', 'A001'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew', 'B001'),
        ('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter', 'B001'),
        ('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter', 'A001')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        # delete all existing jobs
        # database.execute_sql('DELETE FROM job')

        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name = job[job_name],
                    start_date = job[start_date],
                    end_date = job[end_date],
                    salary = job[salary],
                    person_employed = job[person_employed],
                    department = job[department_number])
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def pretty_print_departments():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    logger.info('Print Job class with related departments')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job)
                 .join(Job, JOIN.INNER)
                )

        logger.info('View matching records from both tables')
        for person in query:
            d1 = person.job.department.start_date
            # print(d1) # 2001-09-22
            d2 = person.job.department.end_date
            dd1 = datetime.strptime(d1, "%Y-%m-%d")
            dd2 = datetime.strptime(d2, "%Y-%m-%d")
            delta = dd2 - dd1
            # print('days: ', delta.days)
            logger.info(f'Person {person.person_name} had job {person.job.job_name} in {person.job.department.name} for {delta.days} days')




    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    # populate_departments()
    # populate_jobs()
    pretty_print_departments()
