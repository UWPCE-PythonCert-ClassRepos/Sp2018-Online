import logging
from peewee import *
from datetime import datetime
from src.data_model import Person, Donation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def populate_person():
    """
    add person data to database
    """

    database = SqliteDatabase('mailroom.db')
    logger.info('Working with Person class')

    USERNAME = 0
    PERSON_FIRST_NAME = 1
    PERSON_LAST_NAME = 2

    people = [
        ('anha','Andrew', 'Hatfield'),
        ('pesu','Peter', 'Sunday'),
        ('subo','Susan', 'Boston'),
        ('paco','Pam', 'Coventry'),
        ('stbo','Steven', 'Boyle',)
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
                    username = person[USERNAME],
                    person_first_name = person[PERSON_FIRST_NAME],
                    person_last_name = person[PERSON_LAST_NAME])
                new_person.save()
                logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {person[USERNAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

def populate_donation():
    """
    add donation data to database
    """
    database = SqliteDatabase('mailroom.db')
    logger.info('Working with donation class')

    DONATION_DATE = 0
    AMOUNT = 1
    PERSON_DONATED = 2

    donations = [
        ('2017-09-22', 65500, 'Andrew'),
        ('2018-02-01', 70000, 'Susan'),
        ('2018-05-23', 80000, 'Steven'),
        ('2018-06-01', 45900, 'Pam'),
        ('2018-05-14', 45900, 'Peter'),
        ('2017-11-14', 9000, 'Peter')
    ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                    donation_date = donation[DONATION_DATE],
                    donation_amount = donation[AMOUNT],
                    person_donated = donation[PERSON_DONATED])
                new_donation.save()
                logger.info('Database add successful')


    except Exception as e:
        logger.info(f'Error creating = {donation[DONATION_DATE]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()