"""Lesson 08 Activity - Simple persistence and serialization exercise.

Task:
Pick one of the 4 formats only (i.e. Pickle, Shelve, CSV files or JSON).
Create some data (at least 10 rows with about 5 fields in each).
Show how you can read and write data in that format.
For an extra assignment, write a program that reads form one format and
converts to another.
"""

import pickle
import json
import pprint

# sample_data = [{'product': 'Red couch','description': 'Leather low back'},
# {'product': 'Blue couch','description': 'Cloth high back'},
# {'product': 'Coffee table','description': 'Plastic'},
# {'product': 'Red couch','description': 'Leather high back'}]
sample_data = [[79, 31, 68, 33, 31],
               [22, 25, 62, 62, 95],
               [0, 39, 33, 41, 29],
               [13, 23, 17, 1, 88],
               [21, 17, 34, 9, 88],
               [27, 51, 24, 76, 23],
               [42, 64, 29, 37, 57],
               [42, 12, 31, 87, 42],
               [48, 1, 44, 98, 2],
               [53, 21, 12, 67, 49]]


def to_pickle(filename):
    """Write data to pickle file"""

    try:
        with open(filename, "wb") as to_file:
            pickle.dump(sample_data, to_file)
    except IOError:
        raise "Error: unable to dump data to pickle file"


def from_pickle(filename):
    """Read with pickle"""

    try:
        with open(filename, "rb") as from_file:
            db = pickle.load(from_file)
    except IOError:
        raise "Error: unable to read data from pickle file"

    return db


def from_pickle_to_json(from_filename, to_filename):
    """Read data from a pickle file and save it as a json file."""
    data = from_pickle(from_filename)
    try:
        with open(to_filename, "w") as to_file:
            json.dump(data, to_file, indent=4)
    except IOError:
        raise "Error: unable to dump data to json file"


if __name__ == "__main__":
    filename_pickle = "sample_pickle.pickle"
    to_pickle(filename_pickle)
    expected_data =  from_pickle(filename_pickle)
    assert sample_data == expected_data
    pprint.pprint(expected_data)

    filename_json = "sample_json.json"
    from_pickle_to_json(filename_pickle, filename_json)

    try:
        with open(filename_json, "r") as from_file:
            expected_data_from_json = json.load(from_file)
    except IOError:
        raise "Error: unable to read data from pickle file"

    assert sample_data == expected_data_from_json
    pprint.pprint(expected_data_from_json)
