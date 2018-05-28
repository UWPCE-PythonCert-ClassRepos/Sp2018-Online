"""This module should be used only once to put initial data into DB.

The DB is created by first running models.py in the same directory.
"""

from models import Person, Donation


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
