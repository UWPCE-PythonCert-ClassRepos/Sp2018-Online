"""
Mailroom DB Init

Describes the classes necessary to instantiate the database for mailroom
and populates it with the default information.
"""

import logging
import login_database
import utilities

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')
logger.info('Here we define our data (the schema)')


if __name__ == '__main__':

    try:

        with login_database.login_mongodb_cloud() as client:
            logger.info('Step 1: We are going to use a database called dev')
            logger.info('But if it doesnt exist mongodb creates it')
            db = client['dev']

            logger.info('Reinitialize database')
            db.drop_collection('donation')
            logger.info(
                'And in that database use a collection called donation')
            logger.info('If it doesnt exist mongodb creates it')

            donation = db['donation']

            logger.info("Populating Donation database.")

            donations = [
                {'name': "William Gates III",
                 'email': "bill.gates@msn.com",
                 'donations': [
                     {'date': "2015-01-01", 'value': 653772.32},
                     {'date': "2016-01-01", 'value': 12.17}
                 ]},
                {'name': "Jeff Bezos",
                 'email': "bezos@amazon.com",
                 'donations': [
                     {'date': "2017-01-01", 'value': 877.33}
                 ]},
                {'name': "Paul Allen",
                 'email': "paul.allen@hotmail.com",
                 'donations': [
                     {'date': "2015-01-01", 'value': 663.23},
                     {'date': "2016-01-01", 'value': 43.87},
                     {'date': "2017-01-01", 'value': 1.32}
                ]},
                {'name': "Mark Zuckerberg",
                 'email': "zuck@facebook.com",
                 'donations': [
                     {'date': "2015-01-01", 'value': 1663.23},
                     {'date': "2016-01-01", 'value': 4300.87},
                     {'date': "2017-01-01", 'value': 10432.00}
                 ]
                 }
            ]
            donation.insert_many(donations)
            logger.info("Database add successful")

    except Exception as e:
        logger.info(e)