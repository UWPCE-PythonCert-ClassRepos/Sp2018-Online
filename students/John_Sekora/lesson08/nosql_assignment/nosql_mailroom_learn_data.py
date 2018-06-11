"""
    Data for mongodb database
"""


def get_donor_list_mongodb():
    """
    donor data
    """

    donor_list_mongodb = [
        {
            'person': 'John Smith',
            'donations': [400],
        },
        {
            'person': 'Bill Wilmer',
            'donations': [8000, 10000, 3000],
        },
        {
            'person': 'George Guy',
            'donations': [50],
        },
        {
            'person': 'Nathan Star',
            'donations': [250.50, 100],
        }
    ]

    return donor_list_mongodb
