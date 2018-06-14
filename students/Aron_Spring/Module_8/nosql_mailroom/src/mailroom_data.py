"""
    Data for database demonstrations
"""


def get_donor_data():
    """
    demonstration data
    """

    donor_data = [
        {
            'First_Name': 'Bob',
            'Last_Name': 'Burger',
            'City': 'Seattle'
        },
        {
            'First_Name': 'Joan',
            'Last_Name': 'Sandwich',
            'City': 'Tacoma'
        },
        {
            'First_Name': 'Scott',
            'Last_Name': 'Hotdog',
            'City': 'Kirkland'
        },
        {
            'First_Name': 'Jean',
            'Last_Name': 'Burrito',
            'City': 'Bellevue'
        },
        {
            'Name': 'Summer',
            'City': 'Seattle',
            'Donation': [
                {'Date':'06-06-2018', 'Ammount': '100.00' }
                        ]
        }
    ]
    return donor_data
