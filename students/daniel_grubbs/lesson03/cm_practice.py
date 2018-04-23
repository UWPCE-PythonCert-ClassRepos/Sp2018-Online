#!/usr/bin/env python3
"""
Practice playing around with context managers.

Reference: Python 201: Intermediate Python by Michael Driscoll

"What is a context manager? They are handy constructs that allow you to set something up
and tear something down automatically."

Classic example is using the with statement when working with files.
"""
# Creating a context manager class - This context manager will create a SQLite database connection and close it
# when it;s done.
import sqlite3
import os


class DataConn(object):
    """
    create a SQLite database connection and close it when it's done.
    """

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    # Using the Python magic methods the help identify this as a context manager
    # __enter__() and __exit()__
    def __enter__(self):
        """Open the database connection"""
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the database connection"""
        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db = "{}/test.db".format(dir_path)
    with DataConn(db) as conn:
        cursor = conn.cursor()
