"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

import logging
from peewee import *
from dbase_model import Person, Job, Department


def main():
    """
    add person data to database
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
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Person:
            logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} ' + \
                        f'and likes to be known as {saved_person.nickname}')

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

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

    logger.info('Working with Department class')
    logger.info('Creating Department records: just like Jobs. We use the foreign key')

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

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    main()
