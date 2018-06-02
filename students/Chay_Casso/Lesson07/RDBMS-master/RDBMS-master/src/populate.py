"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

from peewee import *
from v00_personjob_model import Person, Job, Department
from datetime import datetime
import pprint
import logging

def dates_duration(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    return abs((end_date - start_date).days)


def populate_db():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    logger.info("Working with Department class")
    logger.info("Creating Department Records")

    department_code = 0
    department_name = 1
    department_manager = 2

    departments = [
        ("A001", "Sales", "Susan"),
        ("A002", "Support", "Pam"),
        ("A003", "HR", "Steven")
    ]


    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')
    logger.info("Added time_held and reference to department_employed here")

    job_name = 0
    start_date = 1
    end_date = 2
    time_held = 3
    salary = 4
    person_employed = 5
    department_employed = 6

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30',
         dates_duration('2001-09-22', '2003-01-30'), 65500, 'Andrew', 'A001'),
        ('Senior analyst', '2003-02-01', '2006-10-22',
         dates_duration('2003-02-01', '2006-10-22'), 70000, 'Andrew', 'A001'),
        ('Senior business analyst', '2006-10-23', '2016-12-24',
         dates_duration('2006-10-23', '2016-12-24'), 80000, 'Andrew', 'A001'),
        ('Admin supervisor', '2012-10-01', '2014-11-10',
         dates_duration('2012-10-01', '2014-11-10'), 45900, 'Peter', 'A002'),
        ('Admin manager', '2014-11-14', '2018-01-05',
         dates_duration('2014-11-14', '2018-01-05'), 45900, 'Peter', 'A002')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_department = Department.create(
                    department_code = department[department_code],
                    department_name = department[department_name],
                    department_manager = department[department_manager]
                )
                new_department.save()
        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name = job[job_name],
                    start_date = job[start_date],
                    end_date = job[end_date],
                    time_held = job[time_held],
                    salary = job[salary],
                    person_employed = job[person_employed],
                    department_employed = job[department_employed])
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

def print_info():
    """
    connects to database and queries/prints list of users, jobs, and departments.
    :return: printed list of users, jobs, and departments
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person.person_name, Job.job_name, Department.department_name)
                 .join(Job)
                 .join(Department)
                 .tuples()
                 )
        for record in query:
            pprint.pprint(record)

    except Exception as e:
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    # populate_db()
    print_info()