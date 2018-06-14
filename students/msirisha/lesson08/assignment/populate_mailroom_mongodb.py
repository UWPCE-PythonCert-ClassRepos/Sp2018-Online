import logging
import login_database
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def populate_db():
    """
    """

    donor_data = [
        {'uuid': str(uuid.uuid4()), 'donor_name': 'sai emani', 'donations': [20.23, 30.456, 50.786]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'sirisha marthy', 'donations': [67.89, 45.89]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'ani emani', 'donations': [12.789, 5.456]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'Charles Dickens', 'donations': [15.89, 89.20, 345.67]},
        {'uuid': str(uuid.uuid4()), 'donor_name': 'mark twain', 'donations': [678.986]},
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
