"""Populate the DB with department data."""

import logging
from peewee import *
from datetime import date
from .personjobdept_model import Department, Job


def populate_db():
    """Add department data to database."""

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Department class')

    dept_num = 0
    dept_name = 1
    dept_manager_name = 2
    job_held = 3

    departments = [
        ('S002', 'Planning', 'Bruce Willis', 'Analyst'),
        ('S002', 'Planning', 'Bruce Willis', 'Senior analyst'),
        ('S002', 'Strategy', 'Bruce Willis', 'Senior business analyst'),
        ('A001', 'Administration', 'Eric Cartman', 'Admin supervisor'),
        ('A001', 'Administration', 'Eric Cartman', 'Admin manager'),
                  ]

    logger.info('Create Department records: iterate through a list of tuples')
    logger.info('and calculate the number of days in a job by using Job table')
    logger.info('There is also a safeguard to prevent duplication of records')

    def calculate_days(date1, date2):
        """Return difference in days between two dates from the db."""
        date_one = date(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
        date_two = date(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))
        return abs((date_one - date_two).days)

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            with database.transaction():
                # Here I get the relevant job record to calculate days in job
                job = Job.get(Job.job_name == dept[job_held])
                days_in_job = calculate_days(job.start_date, job.end_date)
                # Here I check if such record already exists (since no PK here)
                check_query = (Department
                               .select()
                               .where(
                                   (Department.dept_num == dept[dept_num]) &
                                   (Department.dept_name == dept[dept_name]) &
                                   (Department.dept_manager_name == dept[dept_manager_name]) &
                                   (Department.days_in_job == days_in_job) &
                                   (Department.job_held == dept[job_held])
                                      )
                               )
                if check_query.exists():
                    logger.info('Returned from dept populate_db() because Department record already exists')
                    return
                # Now create the record
                new_dept = Department.create(
                    dept_num=dept[dept_num],
                    dept_name=dept[dept_name],
                    dept_manager_name=dept[dept_manager_name],
                    days_in_job=days_in_job,
                    job_held=dept[job_held])

                new_dept.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_dept in Department:
            logger.info(f'{saved_dept.dept_num}-{saved_dept.dept_name} ' +
                        f'headed by {saved_dept.dept_manager_name}; ' +
                        f'Days job held: {saved_dept.days_in_job}; ' +
                        f'Job held title: {saved_dept.job_held.job_name}')

    except Exception as e:
        logger.info(f'Error creating = {dept[dept_num]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
