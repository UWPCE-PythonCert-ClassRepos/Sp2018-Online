"""Lesson07activity - Create a department table for the db and query the db.

In this exercise, based on instructor-provided code, a very simply
HR-like database is created.
The db contains 3 tables:
    person (PK: person name)
    job (PK: job name; FK: person name)
    department (no PK 'cos no unique fields; FK: job name)

From Activity description: "Finally, produce a list using pretty print that
shows all of the departments a person worked in for every job they ever had."

In this exercise, I wrote pprint_depts.py  and populate_debt_db.py
and modified personjobdept_model.py.
"""
from peewee import *

from RDBMS.personjobdept_model import Person, Job, Department
from RDBMS.populate_person_db import populate_db as populate_people
from RDBMS.populate_job_db import populate_db as populate_jobs
from RDBMS.populate_dept_db import populate_db as populate_departments

# Populate the databe
populate_people()
populate_jobs()
populate_departments()


def pretty_print_person_job_dept(query):
    """Print a list using a query from the db in about the following format.

    Person_1
      worked as Title_1 at Department_1 for XX days
      worked as Title_2 at Department_1 for XX days
    Person_2
       had no jobs
    """
    print('\n')
    for person in query:
        print(person.person_name)
        if len(person.was_filled_by) > 0:
            for job in person.was_filled_by:
                print(f' worked as {job.job_name}', end=' ')
                for dept in job.job_held_at:
                    print(f'at {dept.dept_name} for {dept.days_in_job} days')
        else:
            print('  had no jobs')
    print('\n')

# QUERY 1: using prefetch() - all people, with or w/out jobs
people = Person.select().order_by(Person.person_name)
positions = Job.select().order_by(Job.job_name)
org_units = Department.select().order_by(Department.dept_name)
query1 = prefetch(people, positions, org_units)

# QUERY 2: using join() - only people with jobs are included
query2 = (Person
          .select(Person, Job, Department)
          .join(Job)
          .join(Department)
          .group_by(Person)
          .order_by(Person.person_name)
          )

# QUERY 3: using join() - all people are included with JOIN.LEFT_OUTER
query3 = (Person
          .select(Person, Job, Department)
          .join(Job, JOIN.LEFT_OUTER)
          .join(Department, JOIN.LEFT_OUTER)
          .group_by(Person)
          .order_by(Person.person_name)
          )

for query in (query1, query2, query3):
    pretty_print_person_job_dept(query)
