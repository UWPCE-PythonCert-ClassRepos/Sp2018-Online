"""
    Query a list using pretty print that shows all of the departments
    a person worked in for every job they ever had.
"""

from peewee import *
from pprint import *
from pt1_activity_personjob_dep_model import Person, Job, Department


def query():

    database = SqliteDatabase('personjob.db')
    database.connect()

    database.execute_sql('PRAGMA foreign_keys = ON;')
    every_job = (Person.select(Person, Job, Department)
                 .join(Job, JOIN.INNER)
                 .join(Department, JOIN.INNER)
                 )

    for item in every_job:
        pprint(f'{item.person_name} worked in the {item.job.department.dept_name} ' +
               f'department working as {item.job.job_name}')

    database.close()


if __name__ == '__main__':
    query()
