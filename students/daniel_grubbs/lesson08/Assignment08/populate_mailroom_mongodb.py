"""
    Data for Donor Management System database - MongoDB
"""

import login_database
import utilities

log = utilities.configure_logger('default', 'logs/mongodb_script.log')

def populate_donor_data():
    """
    Populate donor data
    """
    # Define our initial donor data
    donor_data = [
        {
            'donor': 'Jimmy Nguyen',
            'city': 'Houston',
            'donations': [3772.32, 12.17]
        },
        {
            'donor': 'Steve Smith',
            'city': 'Seattle',
            'donations': [877.33, 55.67]
        },
        {
            'donor': 'Julia Norton',
            'city': 'Portland',
            'donations': [663.23, 43.87, 1.32]
        },
        {
            'donor': 'Ed Johnson',
            'city': 'Atlanta',
            'donations': [1663.23, 4300.87, 10432.15]
        },
        {
            'donor': 'Elizabeth McBath',
            'city': 'Austin',
            'donations': [1663.23, 4300.87, 10432.25]
        }
    ]

    try:
        with login_database.login_mongodb_cloud() as client:
            log.info('Step 1: We are going to use a database called dev')
            log.info('But if it doesnt exist mongodb creates it')
            db = client['dev']

            log.info('And in that database use a collection called mailroom')
            log.info('If it doesnt exist mongodb creates it')

            mailroom = db['mailroom']
            mailroom.insert_many(donor_data)
        log.info('Database created successfully with initial donors')
    except Exception as e:
        log.info('Error in creating database with initial donors')
        log.info(e)
    finally:
        log.info('closed the database')


if __name__ == '__main__':
    log.info('running function to populate data')
    populate_donor_data()

