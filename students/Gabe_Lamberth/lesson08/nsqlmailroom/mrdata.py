#!/usr/bin/env python3

"""
    Data for database demonstrations
"""


def get_mailroom_data():
    """
    mailroom data
    """

    mailroom_data = [{'name': {'first': 'Burt', 'last':  'Reynolds'},
                      'donation': [5000.00, 2500.45, 3200.00],
                      'notes': 'High Profile Client'
                      },
                     {'name': {'first': 'Sally', 'last': 'Field'},
                      'donation': [300.25],
                      'notes': 'Drama queen and one time donor'
                      },
                     {'name': {'first': 'Sean', 'last': 'Connery'},
                      'donation': [500.50, 1000.00],
                      'notes': 'The Pen is mightier'
                      }
                     ]

    return mailroom_data