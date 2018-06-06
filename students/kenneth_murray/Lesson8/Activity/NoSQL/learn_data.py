#!/usr/bin/env python3
"""
    Data for database demonstrations
    lesson 8 activity update
    Add more furniture
    separate the product field in to 2 fields; one called product type, one called color.
    Start by amending the data,
    then change the Mongodb program to store and retrieve using these new values.
    Next, write a mongodb query to retrieve and print just the red products, an the just the couches.
"""


def get_furniture_data():
    """
    demonstration data
    """

    furniture_data = [
        {
            'product': 'couch',
            'color': 'red',
            'description': 'Leather low back',
            'monthly_rental_cost': 12.99,
            'in_stock_quantity': 10
        },
        {
            'product': 'Lamp',
            'color': 'purple',
            'description': 'table lamp',
            'monthly_rental_cost': 20.99,
            'in_stock_quantity': 8
        },
        {
            'product': 'couch',
            'color': 'blue',
            'description': 'Cloth high back',
            'monthly_rental_cost': 9.99,
            'in_stock_quantity': 3
        },
        {
            'product': 'table',
            'color': 'coffee',
            'description': 'Plastic',
            'monthly_rental_cost': 2.50,
            'in_stock_quantity': 25
        },
        {
            'product': 'couch',
            'color': 'red',
            'description': 'Leather high back',
            'monthly_rental_cost': 15.99,
            'in_stock_quantity': 17
        },
        {
            'product': 'recliner',
            'color': 'blue',
            'description': 'Leather high back',
            'monthly_rental_cost': 19.99,
            'in_stock_quantity': 6
        },
        {
            'product': 'Chair',
            'color': 'clear',
            'description': 'Plastic',
            'monthly_rental_cost': 1.00,
            'in_stock_quantity': 45
        }
    ]
    return furniture_data
