"""
    mongodb example
"""

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

        log.info('Step 3: Find the products that are described as plastic')
        query = {'description': 'Plastic'}
        results = furniture.find_one(query)

        log.info('Step 4: Print the plastic products')
        print('Plastic products')
        pprint.pprint(results)

        log.info('Step 5: Find the products with product type couch')
        query = {'product type': 'Couch'}
        results = furniture.find_one(query)

        log.info('Step 6: Print the couch products')
        print('Couch types')
        pprint.pprint(results)

        log.info('Step 7: Find the products with color red')
        query = {'product color': 'Red'}
        results = furniture.find_one(query)

        log.info('Step 8: Print the red products')
        print('Red products')
        pprint.pprint(results)

        log.info('Step 9: Delete the white dresser (actually deletes all white items)')
        furniture.remove({"product color": {"$eq": "White"}})

        log.info('Step 10: Check it is deleted with a query and print')
        query = {'product color': 'White'}
        results = furniture.find_one(query)
        print('The white products are deleted, print should show none:')
        pprint.pprint(results)

        log.info(
            'Step 11: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product type']} Stock: {doc['in_stock_quantity']}")

        log.info('Step 12: Delete the collection so we can start over')
        db.drop_collection('furniture')
