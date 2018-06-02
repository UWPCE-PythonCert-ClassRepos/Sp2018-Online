#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mongodb_donor.py
# Dev: Scott Luse
# -------------------------------------------------#

import pprint
import login_database
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_donor.log')


def donor_create_update(gift_amount, donor_name):
    """
    mongodb add donor record
    """

    with login_database.login_mongodb_cloud() as client:
        log.info('Add donor: login')
        db = client['dev']
        donor = db['donor']

        donor_data = [
            {
                'name': donor_name,
                'gift': gift_amount,
                'address': 'empty',
            }
        ]

        log.info('Add donor: insert new record')
        donor.insert_many(donor_data)

        # Show all the records for name
        query = {'name': donor_name}
        results = donor.find_one(query)
        print('Donor gifts to date:')
        pprint.pprint(results)

        cursor = donor.find({'name': donor_name}).sort('gift', 1)
        for doc in cursor:
            print(f"Name: {doc['name']} Donation: {doc['gift']} Address: {doc['address']}")

        db.logout()

def donor_screen_report():
    """
    mongodb screen reporting
    """
    with login_database.login_mongodb_cloud() as client:
        log.info('Screen Report: login')
        db = client['dev']
        donor = db['donor']

        cursor = donor.find({'gift': {'$ne': "a"}})
        for doc in cursor:
            print(f"Name: {doc['name']} Donation: {doc['gift']} Address: {doc['address']}")

        db.logout()

def donor_delete_entry(gift_amount, donor_name):
    """
    mongodb delete single entry
    """
    with login_database.login_mongodb_cloud() as client:
        log.info('Screen Report: login')
        db = client['dev']
        donor = db['donor']

        print("Records found for : " + donor_name)
        cursor = donor.find({'name': {'$eq': donor_name}})
        for doc in cursor:
            print(f"Name: {doc['name']} Donation: {doc['gift']}")

        donor.remove({"name": {"$eq": donor_name}}, {"gift": {"$eq": gift_amount}})

        print("After deletion, these records are found for : " + donor_name)
        cursor = donor.find({'name': {'$eq': donor_name}})
        for doc in cursor:
            print(f"Name: {doc['name']} Donation: {doc['gift']}")

        db.logout()


def donor_drop_collection():
    """
    mongodb drop collection
    """
    with login_database.login_mongodb_cloud() as client:
        log.info('Drop collection: login')
        db = client['dev']
        donor = db['donor']
        db.drop_collection('donor')
