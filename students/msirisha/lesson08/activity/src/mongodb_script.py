"""
    mongodb example
"""

import learn_data
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

        log.info('Step 3: Find the products that are with color red')
        query = {'color': 'Red'}
        cursor = furniture.find(query)

        log.info("Step 4: Print Red items")
        for doc in cursor:
            print(f"Color: {doc['color']} product name:{doc['product']} Description: {doc['description']}")

        log.info('Step 5: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'product': {'$eq' : 'couch'}})
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        print('Couches:')
        for doc in cursor:
            print(f"Color: {doc['color']} product name:{doc['product']} Description: {doc['description']}")

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')

if __name__ == "__main__":
    furn_dict = learn_data.get_furniture_data()
    run_example(furn_dict)
