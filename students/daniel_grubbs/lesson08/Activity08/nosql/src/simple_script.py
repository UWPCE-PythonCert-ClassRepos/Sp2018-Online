"""
pickle etc
"""

import json
import random
import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_json(l):
    log.info("\n\n====")
    log.info("Step 10: Look at working with json data")
    furniture = [{'product': 'Red couch', 'description': 'Leather low back'},
                 {'product': 'Blue couch', 'description': 'Cloth high back'},
                 {'product': 'Coffee table', 'description': 'Plastic'},
                 {'product': 'Red couch', 'description': 'Leather high back'}]

    log.info("Step 11: Return json string from an object")
    furniture_string = json.dumps(furniture)

    log.info("Step 12: Print the json")
    pprint.pprint(furniture_string)

    log.info("Step 13: Returns an object from a json string representation")
    furniture_object = json.loads(furniture_string)
    log.info("Step 14: print the string")
    pprint.pprint(furniture_object)


if __name__ == '__main__':
    data = []
    colors = ['red', 'yellow', 'black', 'pink', 'purple', 'maroon']

    for item in range(10):
        prod = {'product_id': '0{}-HOU'.format(item),
                'color': '{}'.format(random.choice(colors)),
                'description': 'This is item number {}'.format(item),
                'quantity': 10 * item,
                'another_field': (item * item + 3)}
        data.append(prod)

    pprint.pprint(data)
    run_json(data)
