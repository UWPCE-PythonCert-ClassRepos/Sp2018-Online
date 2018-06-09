"""
    Print DB content
"""
from peewee import *
from act7_model import Person, Job, Department
from pprint import pprint

def main():

    database = SqliteDatabase('act7.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job, Department)
                 .join(Job, JOIN.INNER)
                 .join(Department, JOIN.INNER)
                )

        for line in query:
            pprint(f'This employee {line.person_name} had this job {line.job.job_name} in {line.job.department.department_name} department')

    except Exception as e:
        print (e)

    finally:
        database.close()

if __name__ == '__main__':
    main()