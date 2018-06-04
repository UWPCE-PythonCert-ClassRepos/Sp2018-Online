import logging
from peewee import *
from datetime import datetime
from act7_model import Person, Job, Department

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def populate_person():
    """
    add person data to database
    """

    database = SqliteDatabase('act7.db')

    logger.info('Working with Person class')

    PERSON_NAME = 0
    LIVES_IN_TOWN = 1
    NICKNAME = 2

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
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                new_person.save()
                logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

def populate_job():
    """
    add job data to database
    """
    database = SqliteDatabase('act7.db')
    logger.info('Working with Job class')

    job_name = 0
    start_date = 1
    end_date = 2
    salary = 3
    person_employed = 4

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Susan'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Steven'),
        ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 'Pam'),
        ('Admin manager', '2014-11-14', '2018-01-05', 45900, 'Peter')
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
                    person_employed=job[person_employed])
                new_job.save()
                logger.info('Database add successful')


    except Exception as e:
        logger.info(f'Error creating = {job[job_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def populate_department():
    """
        add department data to database
        """
    database = SqliteDatabase('act7.db')
    logger.info('Working with Dept class')

    department_number = 0
    department_name = 1
    department_manager = 2
    job_title = 3

    depts = [
        ('IN01', 'HR', 'Bob B.', 'Analyst'),
        ('HR01', 'IT', 'Tmp X.', 'Admin supervisor'),
        ('IN02', 'Finance', 'Foo B.', 'Senior analyst'),
        ('HR02', 'Eng', 'Zoo K.', 'Admin manager'),
        ('BR01', 'IT', 'Bar G.', 'Senior business analyst')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in depts:
            with database.transaction():
                job = Job.get(Job.job_name == dept[job_title])
                duration_days = calc_num_days(job.start_date, job.end_date)
                new_dept = Department.create(
                    dept_num=dept[department_number],
                    dept_name=dept[department_name],
                    dept_mgr_name=dept[department_manager],
                    days_on_job=duration_days,
                    job_name=dept[job_title])
                new_dept.save()
                logger.info('Add to Department table successful')

    except Exception as e:
        logger.info(f'Error creating = {dept[dept_num]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

def calc_num_days (start_date, end_date):
    return (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days


def populate_db():

    populate_person()
    populate_job()
    populate_department()

if __name__ == '__main__':
    populate_db()