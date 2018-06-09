#!/usr/bin/env python3
"""

pytest file for activity 8

Usage: pytest -k test_hello
    pytest -k test_mongo_insert
"""

# from learn_data import get_furniture_data
# from mongodb_script import run_example

# import learn_data
from learn_data import *
from mongodb_script import *
from login_database import *

# import src.login_database

import redis_script
import neo4j_script
import simple_script
import utilities

def test_mongo_insert():
    furniture_items = get_furniture_data()

    with login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called dev')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['dev']

        log.info('And in that database use a collection called furniture')
        log.info('If it doesnt exist mongodb creates it')

        furniture = db['furniture']

        log.info('Step 2: Now we add data from the dictionary above')
        furniture.insert_many(furniture_items)

        log.info('Step 3: Find the products that are described as plastic')
        query = {'description': 'Plastic'}
        results = furniture.find_one(query)

        log.info('Step 4: Print the plastic products')
        print('Plastic products')
        pprint.pprint(results)

        log.info('Step 5: Delete the blue couch (actually deletes all blue couches)')
        furniture.remove({"product": {"$eq": "Blue couch"}})

        log.info('Step 6: Check it is deleted with a query and print')
        query = {'product': 'Blue couch'}
        results = furniture.find_one(query)
        print('The blue couch is deleted, print should show none:')
        pprint.pprint(results)

        log.info(
            'Step 7: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')


def test_hello():
    print('hello')
    assert 2 == 2, "basic test should pass"


if __name__ == '__main__':
    test_mongo_insert()
    pass
    """
    orchestrate nosql examples
    """
    # furniture = learn_data.get_furniture_data()
    # showoff_databases()
