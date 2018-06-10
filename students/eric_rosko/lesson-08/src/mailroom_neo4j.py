#!/usr/bin/env python3

'''
Author:     Eric Rosko
Lesson:     Session 8
Date:       june 4, 2018
Description:
    Session 8 homework.  This is my ne94j implementation of the mailroom
    program.

File:       ./mailroom_neo4j.py

'''

import logging
from peewee import *
from operator import *
import io
import login_database
import pprint
import utilities
import learn_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting logger...')
logger.setLevel(logging.WARNING)


def add_donation():
    fullname = input("Enter name of donor: ")
    amount = input("Enter donation amount: ")
    mailroom.add_donation(fullname, amount)

    list_donations()


def list_donations():
    print("Current list of donations: ")
    print(mailroom.printable_donations())
    print()


def rename_donor():
    old_name = input("Enter current name of donor: ")
    new_name = input("Enter new name of donor:")
    mailroom.rename_donations(old_name, new_name)

    list_donations()


def delete_donor():
    fullname = input("Enter name of donor to delete: ")
    mailroom.delete_donations(fullname)
    list_donations()


def store_secret():
    fullname = input("Enter name of donor: ")
    secret = input("Enter the secret data to temporarily store: ")
    mailroom.store_temporary_data(fullname, secret)


def retrieve_secret():
    fullname = input("Enter name of donor to retrieve secret note: ")
    print("THE SECRET IS:", mailroom.retrieve_temporary_data(fullname))


class MailroomNeo4j():

    def __init__(self):
        self.driver = None


    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()


    def donor_exists(self, name):
        donors = self.get_donors()
        if name in donors:
            return True

        return False

    def get_session(self):
        if self.driver == None:
            self.driver = login_database.login_neo4j_cloud()
            print("Creating New Driver")
        else:
            print("Using Existing Driver")

        return self.driver.session()


    def add_donor(self, name):
        cyph = "CREATE (n:Donor {name:'%s'})" % (name)
        self.get_session().run(cyph)


    def get_donors(self):
        cyph = """MATCH (p:Donor)
                  RETURN p.name as name
                  ORDER BY name ASC
                """
        result = self.get_session().run(cyph)
        donor_list = []
        for record in result:
            donor_list.append(record['name'])
        return donor_list


    def add_donation(self, donor, amount):
        if not self.donor_exists(donor):
            self.add_donor(donor)

        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cyph = """MATCH (p:Donor{name:'%s'} )
                CREATE (p)-[:GIFT]->(:Donation {amount:'%s'})
                RETURN p
                """ % (donor, amount)

            result = session.run(cyph)


    def get_donations(self, donor):
        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cypher = """MATCH (donor:Donor{name:'%s'})-[:GIFT]->(donation:Donation)
            RETURN donation.amount as amount
            ORDER BY amount ASC""" % (donor)
            result = session.run(cypher)

            # <class 'neo4j.v1.result.BoltStatementResult'>

            list_donations = []

            for x in result:
                list_donations.append(float(x['amount']))

            return list_donations



    def rename_donations(self, old_name, new_name):
        if old_name == new_name:
            return

        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cypher = """MATCH (donor:Donor{name:'%s'})-[:GIFT]->(donation:Donation)
            SET donor.name='%s'
            RETURN donor""" % (old_name, new_name)
            result = session.run(cypher)



    def delete_donations(self, donor):
        # To delete this node, you must first delete its relationships.
        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cypher = """MATCH (donor:Donor{name:'%s'})
            DETACH DELETE donor""" % (donor)
            result = session.run(cypher)


    def printable_donations(self):
        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            cypher = """MATCH (donor:Donor)-[:GIFT]->(donation:Donation)
            RETURN donation.amount as amount, donor.name as name
            ORDER BY name, amount ASC"""
            result = session.run(cypher)

            output = ""

            for doc in result:
                output += f"Donor: {doc['name']}  Amount: ${doc['amount']}\n"

            return output


    def wipe_database(self):
        driver = login_database.login_neo4j_cloud()
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")


    def store_temporary_data(self, donor, secret_data):
        r = login_database.login_redis_cloud()
        r.set(donor, secret_data)


    def retrieve_temporary_data(self, donor):
        r = login_database.login_redis_cloud()
        return r.get(donor)


mailroom = MailroomNeo4j()


if __name__ == "__main__":
    isRunning = True

    while isRunning:
        choice = input("1.) Add donation\n"
                       "2.) Rename donor\n"
                       "3.) Delete donor\n"
                       "4.) Show donors\n"
                       "5.) Store temp data for donor\n"
                       "6.) Retrieve temp data for donor\n"
                       "Choice (q to quit):" )

        if choice == 'q':
            isRunning = False
        elif choice == '1':
            add_donation()
        elif choice == '4':
            list_donations()
        elif choice == '2':
            rename_donor()
        elif choice == '3':
            delete_donor()
        elif choice == '5':
            store_secret()
        elif choice == '6':
            retrieve_secret()
        else:
            print ("Bad input: {}\n".format(choice))
