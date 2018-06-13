"""
    Data for Donor Management System database - Redis
"""

import login_database
import utilities

log = utilities.configure_logger('default', 'logs/redis_script.log')


def populate_donor_data():
    """
    Populate donor data
    """
    # Define our initial donor data
    try:
        log.info('login to redis')
        r = login_database.login_redis_cloud()

        log.info('Push the data to the database')
        r.rpush('Jimmy Nguyen', 'Houston')
        r.rpush('Jimmy Nguyen', '3784.49')

        r.rpush('Steve Smith', 'Seattle')
        r.rpush('Steve Smith', '933')

        r.rpush('Julia Norton', 'Portland')
        r.rpush('Julia Norton', '708.42')

        r.rpush('Ed Johnson', 'Atlanta')
        r.rpush('Ed Johnson', '16396.25')

        r.rpush('Elizabeth McBath', 'Austin')
        r.rpush('Elizabeth McBath', '16396.25')

    except Exception as e:
        log.info('Error in creating database with initial donors')
        log.info(e)
    finally:
        log.info('closed the database')


if __name__ == '__main__':
    log.info('running function to populate data')
    populate_donor_data()
