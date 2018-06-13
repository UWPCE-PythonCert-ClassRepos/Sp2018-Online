"""
    mongodb example
"""

import pprint
import login_database
import utilities

def run_example(donor_list):
    """
    mongodb data manipulation
    """

    with login_database.login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called mailroom')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['mailroom']

        log.info('And in that database use a collection called donors')
        log.info('If it doesnt exist mongodb creates it')

        donors = db['donors']

        log.info('Step 2: Now we add data from the dictionary above')
        donors.insert_many(donor_list)

        log.info('Step 3: Find those with the last name Burger')
        query = {'Last_Name': 'Burger'}
        results = donors.find_one(query)

        log.info('Step 4: Find the donor first names')
        print('Donor matching Burger')
        pprint.pprint(results)

        log.info('Step 5: Find a donation')
        query = {'Name': 'Summer'}
        results = donors.find_one(query)

        log.info('Step 6: Find the donor Summer')
        print('Donor matching Summer')
        pprint.pprint(results)

def add_donor(donor):
    with login_database.login_mongodb_cloud() as client:
        db = client['mailroom']
        donors = db['donors']
        donors.insert_many(donor)
    return donor

def search_donor(donor):
    with login_database.login_mongodb_cloud() as client:
        db = client['mailroom']
        donors = db['donors']
        log.info('Searching for donor')
        query = {'First_Name': donor}
        results = donors.find_one(query)
        pprint.pprint(results)