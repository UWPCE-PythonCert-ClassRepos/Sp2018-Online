#!/usr/bin/env python3

"""
lesson 8
Pick one of the 4 formats only.
Create some data (at least 10 rows with about 5 fields in each).
Show how you can read and write data in that format.
"""
import json
import pprint
import utilities

log = utilities.configure_logger('default', '../logs/simplerick_script.log')


def run_example():
    """
    Json for lesson 8 activity
    """
    def run_json():
        log.info("\n\n====")
        log.info("lesson8: Look at working with json data")
        cars = [{'year': '1967','make': 'ford','model': 'mustang','trim': 'GT','horse power': '90'},
        {'year': '1967','make': 'ford','model': 'mustang','trim': 'GT','horse power': '90'},
        {'year': '1968','make': 'chevrolet','model': 'corvair','trim': 'corsa','horse power': '140'},
        {'year': '1969','make': 'chevrolet','model': 'corvair','trim': 'monza','horse power': '110'},
        {'year': '1970','make': 'opel','model': 'GT','trim': 'GT','horse power': '102'},
        {'year': '1971','make': 'opel','model': 'manta','trim': 'rallye','horse power': '102'},
        {'year': '1972','make': 'opel','model': 'KM5700','trim': 'rallye','horse power': '425'},
        {'year': '1965','make': 'ford','model': 'torino','trim': 'GT','horse power': '10'},
        {'year': '1964','make': 'MG','model': 'B','trim': 'GT','horse power': '90'},
        {'year': '1973','make': 'triumph','model': 'spitfire','trim': 'conv','horse power': '90'},]

        log.info("Return json string from an object")
        cars_string = json.dumps(cars)

        log.info("Step 12: Print the json")
        pprint.pprint(cars_string)

        log.info("Step 13: Returns an object from a json string representation")
        cars_object = json.loads(cars_string)
        log.info("Step 14: print the string")
        pprint.pprint(cars_object)

    run_json()

    return
