"""Create a very simply HR-like database based on instructor-provided code.

Contains 3 tables:
    person (PK: person name)
    job (PK: job name; FK: person name)
    department (no PK 'cos no unique fields; FK: job name)

From Activity description: "Finally, produce a list using pretty print that
shows all of the departments a person worked in for every job they ever had."
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

# Collect records with select()
people = Person.select().order_by(Person.person_name)
positions = Job.select().order_by(Job.job_name)
org_units = Department.select().order_by(Department.dept_name)

# Aggregate multiple tables of records with prefetch()
query = prefetch(people, positions, org_units)

# Produce a list in the following format:
# Person1
#  worked as Position1 at Department1 for XX days
#  worked as Position2 at Department1 for XX days
# Person2
#   had no jobs
for person in query:
    print(person.person_name)
    if len(person.was_filled_by) > 0:
        for job in person.was_filled_by:
            print(f' worked as {job.job_name}', end=' ')
            for dept in job.job_held_at:
                print(f'at {dept.dept_name} for {dept.days_in_job} days')
    else:
        print('  had no jobs')
