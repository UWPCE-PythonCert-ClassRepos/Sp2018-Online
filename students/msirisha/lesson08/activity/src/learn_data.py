"""
    Data for database demonstrations
"""


def get_furniture_data():
    """
    demonstration data
    """

    furniture_data = [
        {
            'product': 'couch',
            'color': 'Red',
            'description': 'Leather low back',
            'monthly_rental_cost': 12.99,
            'in_stock_quantity': 10
        },
        {
            'product': 'couch',
            'color': 'Blue',
            'description': 'Cloth high back',
            'monthly_rental_cost': 9.99,
            'in_stock_quantity': 3
        },
        {
            'product': 'Coffee table',
            'description': 'Plastic',
            'monthly_rental_cost': 2.50,
            'in_stock_quantity': 25
        },
        {
            'product': 'couch',
            'color': 'Red',
            'description': 'Leather high back',
            'monthly_rental_cost': 15.99,
            'in_stock_quantity': 17
        },
        {
            'product': 'recliner',
            'color' : 'Blue',
            'description': 'Leather high back',
            'monthly_rental_cost': 19.99,
            'in_stock_quantity': 6
        },
        {
            'product': 'Chair',
            'description': 'Plastic',
            'monthly_rental_cost': 1.00,
            'in_stock_quantity': 45
        }
    ]
    return furniture_data
