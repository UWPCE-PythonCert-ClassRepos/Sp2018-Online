#!/usr/bin/env python3

'''

These are the unit tests for my implementation of the mailroom class
in mongo db.

Usage: 1.) navigate into src/ first

python3 -m unittest unit-test.py -v

python3 -m unittest -v unit-test.py

python3 -m unittest unittest_mailroom_mongo.MailroomMongoTests

'''

# from unittest import unittest
from unittest import TestCase
from learn_data import *
from mongodb_script import *
from login_database import *
import learn_data

import redis_script
import neo4j_script
import simple_script
import utilities
import json
import pickle
from mailroom_mongo import *

log = utilities.configure_logger('default', '../logs/unit-test.log')

class MailroomMongoTests(TestCase):

    def setUp(self):
        self.mailroom = MailroomMongo()

    def tearDown(self):
        self.mailroom.wipe_database()

    def test_add_donor(self):
        self.mailroom.add_donor("bob")
        # self.assertEqual(True, True)
        donors = self.mailroom.get_donors()

        self.assertEqual(len(donors), 1)
        self.assertEqual(donors[0], 'bob')

    def test_add_donation_for_donor(self):
        self.mailroom.add_donation("bob", 23.54)

        results_count = 0
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']
            cursor = donations.find({"donor": {"$eq": 'bob'}})
            results_count = cursor.count()
        self.assertEqual(results_count, 1)

    def test_get_donations(self):
        self.mailroom.add_donation("bob", 23.54)

        donations = self.mailroom.get_donations("bob")
        self.assertEqual(donations[0], 23.54)

    def test_rename_donor(self):
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)

        self.mailroom.rename_donations("bob", 'jill')
        donations = self.mailroom.get_donations("jill")
        self.assertEqual(len(donations), 2)

    def test_printable_donations(self):
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)
        output = self.mailroom.printable_donations()
        self.assertEqual(output, "Donor: bob  Amount: $23.54\nDonor: bob  Amount: $87.32\n")

    def test_delete_donations(self):
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)
        self.mailroom.delete_donations('bob')
        donations = self.mailroom.get_donations("bob")
        self.assertEqual(len(donations), 0)


if __name__ == "__main__":
    unittest.main()
