"""
    mongodb example
"""

# -------------------------------------------------#
# Title: mongodb_script.py
# Dev: Scott Luse
# Changelog:
# 5/31/2018: split product and color fields, added code
# to retrieve red color items and couch products
# -------------------------------------------------#

import pprint
import login_database
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_example(furniture_items):
    """
    mongodb data manipulation
    """

    with login_database.login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called dev')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['dev']

        log.info('And in that database use a collection called furniture')
        log.info('If it doesnt exist mongodb creates it')

        furniture = db['furniture']

        log.info('Step 2: Now we add data from the dictionary above')
        furniture.insert_many(furniture_items)

        # New code to show the RED with the color field
        log.info('Step 100.1: Find the RED items...')
        query = {'color': 'Red'}
        results = furniture.find_one(query)

        log.info('Step 100.2: Print the RED items...')
        print('RED items...')
        pprint.pprint(results)

        # New code to show the COUCH with the product field
        log.info('Step 200.1: Find the PRODUCT items...')
        query = {'product': 'Couch'}
        results = furniture.find_one(query)

        log.info('Step 200.2: Print the PRODUCT items...')
        print('PRODUCT items...')
        pprint.pprint(results)

        log.info('Step 3: Find the products that are described as plastic')
        query = {'description': 'Plastic'}
        results = furniture.find_one(query)

        log.info('Step 4: Print the plastic products')
        print('Plastic products')
        pprint.pprint(results)

        # New code to show the blue couch with the color field
        log.info('Step 300.1: Find the couch products with NEW color field')
        query = {'product': 'Couch', 'color': 'Blue'}
        results = furniture.find_one(query)

        log.info('Step 300.2: Print the Blue color couches')
        print('Blue Couch...')
        pprint.pprint(results)

        log.info('Step 5: Delete the blue couch using NEW color field')
        # old remove
        # furniture.remove({"product": {"$eq": "Blue couch"}})
        # new remove with both product and color fields
        furniture.remove({"product": {"$eq": "Couch"}}, {"color": {"$eq": "Blue"}})

        log.info('Step 6: Check it is deleted with a query and print')
        # old query
        # query = {'product': 'Blue couch'}
        # new query
        query = {'product': 'Couch', 'color': 'Blue'}

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
