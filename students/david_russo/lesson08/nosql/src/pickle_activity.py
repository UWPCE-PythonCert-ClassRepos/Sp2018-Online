#!/usr/bin/env python3

"""
pickle etc
"""

import pickle

import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')



def run_pickle(data_for_pickle):
    """
    Write and read with pickle
    """
    log.info("\n\n====")
    log.info('Step 1: Demonstrate persistence with pickle')
    log.info('Write a pickle file with the furniture data')

    pickle.dump(data_for_pickle, open('../data/pickling_activity_data.pkl', 'wb'))

    log.info('Step 2: Now read it back from the pickle file')
    read_data = pickle.load(open('../data/pickling_activity_data.pkl', 'rb'))
    log.info('Step 3: Show that the write and read were successful')
    assert read_data == data_for_pickle
    log.info("and print the data")
    pprint.pprint(read_data)

if __name__ == "__main__":
    pickling_data = [
    {'name': 'James Paxton','throws': 'L', 'bats': 'L', 'position': 'P', 'team': 'SEA'},
    {'name': 'Felix Hernandez','throws': 'R', 'bats': 'R', 'position': 'P', 'team': 'SEA'},
    {'name': 'Mike Leak','throws': 'R', 'bats': 'R', 'position': 'P', 'team': 'SEA'},
    {'name': 'Marco Gonzales','throws': 'L', 'bats': 'L', 'position': 'P', 'team': 'SEA'},
    {'name': 'Wade LeBlanc','throws': 'L', 'bats': 'L', 'position': 'P', 'team': 'SEA'},
    {'name': 'Eric Hosmer','throws': 'L', 'bats': 'L', 'position': '1B', 'team': 'SD'},
    {'name': 'Carlos Asuaje','throws': 'R', 'bats': 'L', 'position': '2B', 'team': 'SD'},
    {'name': 'Christian Villanueva','throws': 'R', 'bats': 'R', 'position': '3B', 'team': 'SD'},
    {'name': 'Freddy Galvis','throws': 'R', 'bats': 'S', 'position': 'SS', 'team': 'SD'},
    {'name': 'Manuel Margot','throws': 'R', 'bats': 'R', 'position': 'CF', 'team': 'SD'}
    ]
    
    pprint.pprint(pickling_data)
    run_pickle(pickling_data)


