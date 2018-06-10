"""
pickle etc
"""

import pickle


import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_pickle(sdata):
    """
    Write and read with pickle
    """
    log.info("\n\n====")
    log.info('Step 1: Demonstrate persistence with pickle')
    log.info('Write a pickle file with the furniture data')

    pickle.dump(sdata, open('../data/activity_data.pkl', 'wb'))

    log.info('Step 2: Now read it back from the pickle file')
    read_data = pickle.load(open('../data/activity_data.pkl', 'rb'))
    log.info('Step 3: Show that the write and read were successful')
    assert read_data == sdata
    log.info("and print the data")
    pprint.pprint(read_data)



if __name__ == "__main__":

    simple_data = []

    for d in range(10):
        item = {'product': 'P' + str(d),
                'quantity': d * 10,
                'description': 'Bleh ' * (d + 1),
                'cost': 1.00 + d,
                'location': 'Alpha' + str(d * 2)}
        simple_data.append(item)

    pprint.pprint(simple_data)

    run_pickle(simple_data)


