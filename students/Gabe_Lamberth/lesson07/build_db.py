"""
     Building the DB with data
"""

import logging
from peewee import *
from dbase_model import Person, Job, Department


def main():
    """
    Add person data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('activity7.db')

    logger.info('Working with Person, Job & Department class')
    logger.info('Using constants and a list of tuples as a simple schema')

    person_name = 0
    lives_in_town = 1
    nickname = 2

    people = [
        ('Andrew', 'Sumner', 'Andy'),
        ('Peter', 'Seattle', None),
        ('Susan', 'Boston', 'Beannie'),
        ('Pam', 'Coventry', 'PJ'),
        ('Steven', 'Colchester', None),
    ]

    logger.info('Creating Person records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with database.transaction():
                new_person = Person.create(
                    person_name=person[person_name],
                    lives_in_town=person[lives_in_town],
                    nickname=person[nickname])
                new_person.save()
                logger.info('Add to Person table successful')

        # logger.info('Print the Person records we saved...')
        # for saved_person in Person:
        #     logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} ' + \
        #                 f'and likes to be known as {saved_person.nickname}')

    except Exception as e:
        logger.info(f'Error creating = {person[person_name]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    job_name = 0
    start_date = 1
    end_date = 2
    salary = 3
    person_employed = 4

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew'),
        ('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter'),
        ('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name = job[job_name],
                    start_date = job[start_date],
                    end_date = job[end_date],
                    salary = job[salary],
                    person_employed = job[person_employed])
                new_job.save()
                logger.info('Add to Job table successful')

        # logger.info('Reading and print all Job rows (note the value of person)...')
        # for job in Job:
        #     logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

    logger.info('Working with Department class')
    logger.info('Creating Department records: just like Jobs. We use the foreign key')

    dept_num = 0
    dept_name = 1
    dept_mgr_name = 2
    days_on_job = 3
    job_name = 4


    # Set the days on job value default to 0
    depts = [
        ('IN01', 'Intelligence Division', 'Susan Lee', 0, 'Analyst'),
        ('IN02', 'Intelligence Division Lead', 'Burt Reynolds', 0, 'Senior analyst'),
        ('BR01', 'Finance Department Lead', 'Dolly Parton', 0, 'Senior business analyst'),
        ('HR01', 'Human Resources Lead', 'Chris Watkins', 0, 'Admin supervisor'),
        ('HR02', 'Human Resources Manager', 'Heather Locklear', 0, 'Admin manager')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in depts:
            with database.transaction():
                new_dept = Department.create(
                    dept_num = dept[dept_num],
                    dept_name = dept[dept_name],
                    dept_mgr_name = dept[dept_mgr_name],
                    days_on_job = dept[days_on_job],
                    job_name = dept[job_name])
                new_dept.save()
                logger.info('Add to Department table successful')

        # logger.info('Reading and print all Job rows (note the value of person)...')
        # for dept in Department:
        #     logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {dept[dept_num]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    main()
