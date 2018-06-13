"""
    Reports for each Person, what jobs they had, which department and how long they
    had the job in days
"""

from peewee import *
from v00_personjob_model import Person, Job
from add_dept import Department, Job_Department

import logging
from datetime import datetime
from pprint import pprint


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('./data/personjob.db')

logger.info('View matching records and Persons without Jobs (note LEFT_OUTER)')
# person name, department job, duration

try:
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    query = (Person
             .select(Person.person_name, Job.job_name, Job.start_date, Job.end_date, Job_Department.dept_id)
             .join(Job, JOIN.LEFT_OUTER)
             .join(Job_Department, JOIN.LEFT_OUTER)
            )

    for person in query:
        try:
            duration = (datetime.strptime(person.job.end_date, '%Y-%m-%d') - datetime.strptime(person.job.start_date, '%Y-%m-%d')).days
            logger.info(f'Person {person.person_name} had job {person.job.job_name} for {duration} days in dept: {person.job.job_department.dept_id.name}')

            pprint(f'{person.person_name} had job {person.job.job_name} for {duration} days in dept: {person.job.job_department.dept_id.name}')

        except Exception as e:
            logger.info(f'...Exception was {e}')
            logger.info(f'Person {person.person_name} had no job')

except Exception as x:
    print('hut')
    logger.info(x)

finally:
    database.close()
