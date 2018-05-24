"""
Pretty print all departments a person has worked for every job they've had.
"""

from peewee import *
from RDBMS.personjobdepartment_model import Person, Job, Department
from RDBMS.populate_people_db import populate_db as pop_poeple_db
from RDBMS.populate_jobs_db import populate_db as pop_jobs_db
from RDBMS.populate_department_db import populate_db as pop_dept_db
import logging

# populate the db
pop_poeple_db()
pop_jobs_db()
pop_dept_db()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
database = SqliteDatabase('../personjob.db')

people = Person.select()
jobs = Job.select()
departments = Department.select()


query = (Person
    .select(Person, Job, Department)
    .join(Job, JOIN.LEFT_OUTER)
    .join(Department, JOIN.LEFT_OUTER)
    .group_by(Person, Job)
    )

for person in query:
    print("name: " + person.person_name)
    for job in person.was_filled_by:
        print("\t job title: " + job.job_name)
        for department in job.title_of_job:
            print("\t\t department: " + department.department_name)

