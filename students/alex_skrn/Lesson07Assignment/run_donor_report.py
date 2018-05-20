#!/usr/bin/env python3

"""Running a donor report from a separate program.

Assignment 7, inter alia, suggests the following:
"Remember that you need to read from the database, rather than relying on
data held in variables when your program is running. To show you understand
how this works, run the donor report from a separate program
that read the database."

So I prepared this module in response to this suggestion. And I re-use it
entirely in my mailroom project to load data from DB and convert it into
one of my class objects to be able to apply my methods to manipulate the data.
"""

import peewee
from models import Person, Donation
from RELATIONALMAILROOM.mailroom import SingleDonor, Donors

# Get donor info from db and convert it into Donors class which
# the create_report() method will use to generate the report
dict_donors_gifts = {}
donors = Person.select().order_by(Person.person_name)
donations = Donation.select()
query = peewee.prefetch(donors, donations)
# Iterate over the query and collect all data into a dict
# with donors as keys and donations as lists of values
for donor in query:
    dict_donors_gifts[donor.person_name] = []
    for gift in donor.donations:
        dict_donors_gifts[donor.person_name].append(float(gift.donation))

# Convert the dict with donors as keys and donations as values into
# a Donors class object
class_donors = Donors([SingleDonor(key, value) for key, value in
                      dict_donors_gifts.items()
                       ]
                      )
# Now make use of the create_report() method of the Donors class object
class_donors.create_report()
