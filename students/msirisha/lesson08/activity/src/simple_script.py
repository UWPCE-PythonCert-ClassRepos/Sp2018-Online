"""
pickle etc
"""

import pickle
import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_pickle(data):
    """
    Write and read with pickle
    """
    log.info("\n\n====")
    log.info('Step 1: Demonstrate persistence with pickle')
    log.info('Write a pickle file with the product data')

    pickle.dump(data, open('../data/data.pkl', 'wb'))

    log.info('Step 2: Now read it back from the pickle file')
    read_data = pickle.load(open('../data/data.pkl', 'rb'))
    log.info('Step 3: Show that the write and read were successful')
    assert read_data == data
    log.info("and print the data")
    pprint.pprint(read_data)


if __name__ == "__main__":

    data = []
    for i in range(10):
        item = {'Product': 'P' + str(i+1),
                'Quantity': (i + 1) * 10,
                'Description': 'yay' * (i + 1),
                'Cost': 1 * (i+1),
                'category': 'category' + str(i+1)
                }
        data.append(item)
    run_pickle(data)
