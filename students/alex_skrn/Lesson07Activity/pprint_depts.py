"""Create a db, populate it with people, jobs and departments, and print."""
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

# Lesson 07 activity:
# Produce a list using pretty print that shows all of the departments
# a person worked in for every job they ever had
for person in query:
    print(person.person_name)
    if len(person.was_filled_by) > 0:
        for job in person.was_filled_by:
            print(' worked as', job.job_name, end=' ')
            for dept in job.job_held:
                print('at', dept.dept_name)
    else:
        print('  had no jobs')
