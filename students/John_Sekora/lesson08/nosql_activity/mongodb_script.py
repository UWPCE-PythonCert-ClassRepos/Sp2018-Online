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

        # New Querying for the Activity (Red products and Couches)
        log.info('Retrieving just the Red colored products')
        query_red = {'color': 'Red'}
        results_red = furniture.find_one(query_red)

        log.info('Printing the Red colored products')
        pprint.pprint(results_red)

        log.info('Retrieving just the Couch products')
        query_couch = {'product': 'Couch'}
        results_couch = furniture.find_one(query_couch)

        log.info('Printing the Couch products')
        pprint.pprint(results_couch)

        # Query for plastic description
        log.info('Step 3: Find the products that are described as plastic')
        query_plastic = {'description': 'Plastic'}
        results_plastic = furniture.find_one(query_plastic)

        log.info('Step 4: Print the plastic products')
        print('Plastic products')
        pprint.pprint(results_plastic)

        # Updating query for the revised product fields
        log.info('Step 5: Delete the blue couch (using the "product" and "color" fields)')
        furniture.remove({'product': {'$eq': 'Couch'}}, {'color': {'$eq': 'Blue'}})

        log.info('Step 6: Check it is deleted with a query and print')
        query_couch_blue = {'product': 'Couch', 'color': 'Blue'}
        results_couch_blue = furniture.find_one(query_couch_blue)
        print('The blue couch is deleted, print should show none:')
        pprint.pprint(results_couch_blue)

        log.info('Step 7: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')
