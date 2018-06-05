#!/usr/bin/env python3

'''

Author:     Eric Rosko
Lesson:     Session 8
Date:       june 4, 2018

These are the unit tests for my implementation of the mailroom class
in neo4j db.

Usage: 1.) navigate into src/ first
    python3 -m unittest unit-test.py -v
    python3 -m unittest -v unit-test.py

    python3 -m unittest unittest_mailroom_neo4j.MailroomNeo4jTests

'''
# from unittest import unittest
from unittest import TestCase
from login_database import *
import redis_script
import neo4j_script
from mailroom_neo4j import *

log = utilities.configure_logger('default', '../logs/unit-test.log')

class MailroomNeo4jTests(TestCase):

    def setUp(self):
        self.mailroom = MailroomNeo4j()

    def tearDown(self):
        self.mailroom.wipe_database()

    def test_add_donor(self):
        self.mailroom.add_donor("bob")

        donor_list = self.mailroom.get_donors()

        self.assertEqual(len(donor_list), 1)
        self.assertEqual(donor_list[0], 'bob')

    def test_add_two_donors(self):
        self.mailroom.add_donor("bob")
        self.mailroom.add_donor("jill")

        donor_list = self.mailroom.get_donors()

        self.assertEqual(2, len(donor_list))
        self.assertEqual('bob', donor_list[0])
        self.assertEqual('jill', donor_list[1])

    def test_add_donation_for_donor(self):
        """
        note that a donor has to be added before a donation is added
        """
        self.mailroom.add_donor("bob")
        self.mailroom.add_donation("bob", 23.54)

        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cypher = """MATCH (donor:Donor)-[:GIFT]->(donation:Donation)
            WHERE donor.name='bob'
            RETURN donor.name, donation.amount"""
            result = session.run(cypher)

            # <class 'neo4j.v1.result.BoltStatementResult'>
            print(type(result))

            counter = 0
            for x in result:
                counter += 1
                # X: <Record donor.name='bob' donation.amount='23.54'>
                print("X:", x['donor.name'], x['donation.amount'])
                self.assertEqual('bob', x['donor.name'])
                self.assertEqual('23.54', x['donation.amount'])

            self.assertEqual(1, counter)


    def test_get_donations(self):
        self.mailroom.add_donor("dave")
        self.mailroom.add_donation("dave", 99.99)
        self.mailroom.add_donor("bob")
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 2.99)
        self.mailroom.add_donor("jill")
        self.mailroom.add_donation("jill", 5.49)

        donations = self.mailroom.get_donations("bob")
        self.assertEqual(donations[0], 2.99)
        self.assertEqual(donations[1], 23.54)


    def test_rename_donor(self):
        self.mailroom.add_donor("bob")
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)

        self.mailroom.rename_donations("bob", 'jill')
        donations = self.mailroom.get_donations("jill")
        self.assertEqual(len(donations), 2)
        donations = self.mailroom.get_donations("bob")
        self.assertEqual(0, len(donations))


    def test_printable_donations(self):
        self.mailroom.add_donor("bob")
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)
        output = self.mailroom.printable_donations()
        self.assertEqual("Donor: bob  Amount: $23.54\nDonor: bob  Amount: $87.32\n", output)

    def test_delete_donations(self):
        self.mailroom.add_donor("bob")
        self.mailroom.add_donation("bob", 23.54)
        self.mailroom.add_donation("bob", 87.32)
        self.mailroom.delete_donations('bob')
        donations = self.mailroom.get_donations("bob")
        self.assertEqual(len(donations), 0)


    def test_donor_exists_false(self):
        self.assertFalse(self.mailroom.donor_exists('bob'))
        self.mailroom.add_donor("bob")
        self.assertTrue(self.mailroom.donor_exists('bob'))

if __name__ == "__main__":
    unittest.main()
