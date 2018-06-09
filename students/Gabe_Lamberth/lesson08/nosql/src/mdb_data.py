"""
    Data for database demonstrations
"""


def get_furniture_data():
    """
    demonstration data
    """

    furniture_data = [{'product': {'type': 'couch', 'color': 'red'},
                       'description': 'Leather low back',
                       'monthly_rental_cost': 14.99,
                       'in_stock_quantity': 10
                       },
                      {'product': {'type': 'couch', 'color': 'blue'},
                       'description': 'Leather low back',
                       'monthly_rental_cost': 10.99,
                       'in_stock_quantity': 19
                       },
                      {'product': {'type': 'chair', 'color': 'brown'},
                       'description': 'Leather cup holders, recliner',
                       'monthly_rental_cost': 12.99,
                       'in_stock_quantity': 13
                       },
                      {'product': {'type': 'chair', 'color': 'black'},
                       'description': 'Leather cup holders, recliner',
                       'monthly_rental_cost': 13.99,
                       'in_stock_quantity': 3
                       },
                      {'product': {'type': 'table', 'color': 'brown'},
                       'description': 'Coffee table',
                       'monthly_rental_cost': 7.99,
                       'in_stock_quantity': 5
                       },
                      {'product': {'type': 'table', 'color': 'white'},
                       'description': 'Kitchen',
                       'monthly_rental_cost': 7.99,
                       'in_stock_quantity': 13
                       },
                      {'product': {'type': 'stand', 'color': 'gray'},
                       'description': 'End table for couch',
                       'monthly_rental_cost': 3.99,
                       'in_stock_quantity': 9
                       },
                      {'product': {'type': 'stand', 'color': 'brown'},
                       'description': 'Night stand for bedroom',
                       'monthly_rental_cost': 3.99,
                       'in_stock_quantity': 13
                       },
                      {'product': {'type': 'lamp', 'color': 'silver'},
                       'description': 'Tall living room lamp',
                       'monthly_rental_cost': 2.99,
                       'in_stock_quantity': 1
                       }
                      ]
    return furniture_data
