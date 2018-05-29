"""
"""

import logging
import login_database
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def populate_db():
    """
    """

    donor_data = [
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Al Donor1', 'donations': [10.00, 20.00, 30.00, 40.00, 50.00]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Bert Donor2', 'donations': [10.00]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Connie Donor3', 'donations': [10.00, 10.00, 10.01]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Dennis Donor4', 'donations': [10.00, 20.00, 20.00]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Egbert Donor5', 'donations': [10.39, 20.21, 10.59, 4000.40]},
    ]

    try:
        with login_database.login_mongodb_cloud() as client:
            db = client['dev']
            mailroom = db['mailroom']
            mailroom.insert_many(donor_data)
        logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating MongoDB mailroom database.')
        logger.info(e)

    finally:
        logger.info('database closes')



if __name__ == '__main__':
    populate_db()
    # with login_database.login_mongodb_cloud() as client:
    #     db = client['dev']
    #     db.drop_collection('mailroom')