#!/usr/bin/env python3

'''
Author:     Eric Rosko
Lesson:     Session 8
File:       mailroom.py
Date:       june 3, 2018
Description:
    Session 8 homework.  This is my mongodb implementation of the mailroom
    program.

Usage:
    python3 mailroom.py
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


class MailroomMongo():

    def __init__(self):
        pass


    def add_donor(self, name):
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donors = db['donors']

            results = donors.insert_one({'name': name})


    def get_donors(self):
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donors = db['donors']

            cursor = donors.find({}).sort('name', 1)

            all_donors = []
            for doc in cursor:
                all_donors.append(doc['name'])
                # print(f"Name: {doc['name']}")

            return all_donors


    def add_donation(self, donor, amount):
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']

            result = donations.insert_one({
                      'donor': donor,
                      'amount': amount})
            print("added", result)


    def get_donations(self, donor):
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']

            list_donations = []
            cursor = donations.find({"donor": {"$eq": donor}})
            for doc in cursor:
                # print(doc['amount'], doc['donor'])
                d = doc['amount']
                list_donations.append(d)
            return list_donations


    def rename_donations(self, old_name, new_name):
        if old_name == new_name:
            return

        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']

            cursor = donations.find({"donor": {"$eq": old_name}})
            for doc in cursor:
                d = doc['amount']
                self.add_donation(new_name, d)

            donations.delete_many({"donor": {"$eq": old_name}})


    def delete_donations(self, donor):
        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']

            donations.delete_many({"donor": {"$eq": donor}})


    def printable_donations(self):

        with login_database.login_mongodb_cloud() as client:
            db = client['mailroom']
            donations = db['donations']

            output = ""
            cursor = donations.find({})
            for doc in cursor:
                output += f"Donor: {doc['donor']}  Amount: ${doc['amount']}\n"
                # print(doc['amount'], doc['donor'])

            return output


    def wipe_database(self):
        with login_database.login_mongodb_cloud() as client:
            client['mailroom'].drop_collection('donors')
            client['mailroom'].drop_collection('donations')


    def store_temporary_data(self, donor, secret_data):
        r = login_database.login_redis_cloud()
        r.set(donor, secret_data)


    def retrieve_temporary_data(self, donor):
        r = login_database.login_redis_cloud()
        return r.get(donor)


mailroom = MailroomMongo()


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
