"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        joinn classes
"""

from peewee import *
from v00_personjob_model import Person, Job, Department

import logging
from datetime import date

def join_classes():

    "show all departments a person worked"

    """
        demonstrate how to join classes together : matches
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('data/personjob.db')

    logger.info('Now resolve the join and print (INNER shows only jobs that match person and dep that match job)')
    logger.info('Notice how we use a query variable in this case')
    logger.info('We select the classes we need, and we join Person to Job')
    logger.info('Inner join (which is the default) shows only records that match')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query1 = Person.select(Person, Job).join(Job, JOIN.INNER)






        logger.info('View matching records from tables')
        print("{:30s}|{:30s}|{:15}|{:30}|{:4}".format("Name", "Job", "Duration [days]", "Department", "ID"))
        for person in query1:
            job_start = person.job.start_date
            job_end = person.job.end_date
            y1 = int(job_start.split("-")[0])
            y2 = int(job_end.split("-")[0])
            m1 = int(job_start.split("-")[1])
            m2 = int(job_end.split("-")[1])
            d1 = int(job_start.split("-")[2])
            d2 = int(job_end.split("-")[2])
            job_dur = date(y2, m2, d2) - date(y1, m1, d1)
            dep = Department.get(Department.dep_job == person.job.job_name)

            print("{:30s}|{:30s}|{:15}|{:30}|{:4}".format(person.person_name,
                                                          person.job.job_name,
                                                          job_dur.days,
                                                          dep.dep_name,
                                                          dep.dep_num))

    except Exception as e:
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    join_classes()
