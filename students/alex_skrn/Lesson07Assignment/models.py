"""This module creates a DB for the mailroom project in Lesson 7 (RDBMS).

This module should be run first. Then the module add_data.py should be
run to add initial example data in DB.

Compared to the examples in the Lesson 07 Activity, my solution does not
use such commands as db.connect(), db.execute_sql('PRAGMA foreign_keys = ON;'),
# db.close(), because these things cause the program to attempt to create
the db anew or something like that and generated loads of errors every time
I tried to import db Models from my mailroom module in order
to query or insert data from/into DB.

I found examples in the following blog easy to understand and useful:
https://www.blog.pythonlibrary.org/2014/07/17/an-intro-to-peewee-another-python-orm/
"""

import peewee

# Create a db
db = peewee.SqliteDatabase("mailroom_db.db")

# db.connect()
# db.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Person(BaseModel):
    person_name = peewee.CharField(primary_key=True, max_length=30)

class Donation(BaseModel):
    person_name = peewee.ForeignKeyField(Person, related_name="donations", null=False)
    donation = peewee.DecimalField(max_digits=7, decimal_places=2)

if __name__ == "__main__":
    try:
        db.create_tables([Person, Donation])
    except peewee.OperationalError as e:
        print("Problem creating tables", e)

# db.close()
