"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        populate the DB with data
"""

from peewee import *
from v00_personjob_model import Person, Job, Department

import logging


def populate_db():
    """
        add departments data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('data/personjob.db')

    logger.info('Working with Department class')
    logger.info('Creating Department records: just like Person. We use the foreign key')

    # index used to clearly read code when index on a list of tuple data below
    dep_num = 0
    dep_name = 1
    dep_head = 2
    dep_job = 3

    dep_data = [
        ("0001", "Shipping", "D. Vader", "Analyst"),
        ("0002", "Shipping", "O. Kenobi", "Senior analyst"),
        ("0003", "Shipping", "O. Kenobi", "Senior business analyst"),
        ("0052", "Product Development", "O. Kenobi", "Admin supervisor"),
        ("0053", "Product Development", "O. Kenobi", "Admin manager"),
        ]

    try:
        # open connect to database, db defined above as sqlite + path
        database.connect()
        # not sure what this does
        database.execute_sql('PRAGMA foreign_keys = ON;')
        # load raw data to database
        for dep in dep_data:
            # database.transaction() opens writing (similar to sys file write)
            with database.transaction():
                # create new entry in Department class
                # the Department class inherited from peewee Meta, and has .create for new entry
                new_dep = Department.create(
                    dep_num=dep[dep_num],
                    dep_name = dep[dep_name],
                    dep_head = dep[dep_head],
                    dep_job = dep[dep_job])
                new_dep.save()

        logger.info('Reading and print all Department rows')
        for dep in Department:
            logger.info(f'Job Title: {dep.dep_job} In Department: {dep.dep_name} [{dep.dep_num}], Head: {dep.dep_head}')

    except Exception as e:
        logger.info(f'Error creating = {dep[dep_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


if __name__ == '__main__':
    populate_db()
