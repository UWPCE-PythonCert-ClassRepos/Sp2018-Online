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

        log.info('Step 3: Find the products that are described as couch')
        query = {'product': 'Couch'}
        results = furniture.find(query)

        log.info('Step 4: Print the couch product')
        print('Couch Products')
        for doc in results:
            print(f"{doc['product']} color: {doc['color']}")

        log.info('Step 5: Delete all couch')
        furniture.remove({"product": {"$eq": "Couch"}})

        log.info('Step 6: Check it is deleted with a query and print')
        query = {'product': 'Couch'}
        results = furniture.find_one(query)
        print('All couches are deleted, print should show none:')
        pprint.pprint(results)

        log.info('Step 7: Add a blue couch and print all blue products')
        furniture.insert({
            'product': 'Couch',
            'color': 'Blue',
            'description': 'Gold',
            'monthly_rental_cost': 250,
            'in_stock_quantity': 1
        })
        cursor = furniture.find({'color': {'$eq': 'Blue'}})
        for doc in cursor:
            print(f"{doc['product']} color: {doc['color']}")

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')
