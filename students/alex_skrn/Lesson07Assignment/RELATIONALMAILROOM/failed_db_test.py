"""This test does not work.

This is just to show I was trying to do tests for db-related functionality.

But failed to overcome the initial difficulty of seting up
a sample database and passing it to my tests.

I think I have a  fundamental misunderstanding of how databases operate.
For example, peewee documentation and class videos suggest that using
db.connect() / db.close() are a best practice.
But I was only able to use the db classes imported
into my mailroom file after I removed those commands from the files
which created and populated the database. Otherwise the mailroom program
gave out all sorts of errors when started.
"""

import os
import peewee
import pytest
import random
from mailroom import SingleDonor

@pytest.fixture(scope="function")
def db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test_db.db")

    db = peewee.SqliteDatabase(file)
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

    try:
        db.create_tables([Person, Donation])
    except peewee.OperationalError as e:
        print("Problem creating tables", e)

    def populate_db():
        """Populate DB with initial donor and gifts data."""
        # Populate db with donors - using Model(name=name).save(force_insert=True)
        person_name = 0
        people = [("Bill Murray",),
                  ("Woody Harrelson",),
                  ("Jesse Eisenberg",)
                  ]
        try:
            for person in people:
                new_person = Person(person_name=person[person_name])
                new_person.save(force_insert=True)
                print('add success')

            print('Person length:', len(Person), type(Person))
            for person in Person:
                print('Added name to Person table:', person.person_name)

        except Exception as e:
            print("db probably already exist with these data because", e)
            return

        finally:
            print("In first finally clause")

        # Populate db with donations - using Model(name=name).save() method
        donor_person = 0
        donation = 1
        donations = [("Bill Murray", 125),
                     ("Bill Murray", 1.0),
                     ("Woody Harrelson", 71.5),
                     ("Woody Harrelson", 1.25),
                     ("Jesse Eisenberg", 99.99),
                     ("Jesse Eisenberg", 1.75)
                     ]
        try:
            for gift in donations:
                new_gift = Donation(person_name=gift[donor_person],
                                    donation=gift[donation]
                                    )
                new_gift.save()
                print('add success')

            print('Donation length:', len(Donation), type(Person))
            for gift in Donation:
                print('Added gift to Donation table:', gift.donation)

        except Exception as e:
            print(e)

        finally:
            print("in second finally clause")

    populate_db()

    yield db

    # print(file)

    # person = Person.select()
    # for name in person:
    #     print(name.person_name)
    #     print(name.delete_instance() == 1)

    db.close()
    # os.remove(file)
    # os.remove(tmpdir)


def test_add_donation(db):
    """Test add_donation() method of the SimpleDonor class."""
    # This test doesn't use db I created in pytest.fixture.
    # db.connect()
    donor = SingleDonor("Bill Murray", 125)
    donor.add_donation(300)
    query = Person.get(Person.person_name == "Bill Murray")
    res = []
    for g in query.donations:
        res.append(float(g.donation))
    assert res[-1] == 301 # This is suppposed to  fail
