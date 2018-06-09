"""
    demonstrate use of Redis
"""

# -------------------------------------------------#
# Title: redis_script.py
# Dev: Scott Luse
# Changelog:
# 5/31/2018: added several customers to Redis cache
# retrieve a customer based on zip code and phone number
# -------------------------------------------------#

import login_database
import utilities


def run_example():
    """
        uses non-presistent Redis only (as a cache)

    """

    log = utilities.configure_logger('default', '../logs/redis_script.log')

    try:
        log.info('Step 1: connect to Redis')
        r = login_database.login_redis_cloud()
        log.info('Step 2: cache some data in Redis')
        r.set('andy', 'andy@somewhere.com')

        log.info('Step 2: now I can read it')
        email = r.get('andy')
        log.info('But I must know the key')
        log.info(f'The results of r.get: {email}')

        # Add some customer data to the cache and retrieve
        # Unable to use 'mset' and 'mget' correctly

        log.info('Step 100: cache more CUSTOMER data in Redis###')
        r.set('ironman:phone', '555-1212')
        r.set('ironman:zipcode', '98290')

        r.set('spiderman', '555-1313', '98291')
        r.set('superman', '555-1414', '98292')
        r.set('wonderwoman', '555-1515', '98293')
        r.set('peterpan', '555-1616', '98294')
        r.set('peterparker', '555-1717', '98295')

        zipcode = r.mget('ironman:zipcode')
        log.info(f'The results of r.get: {zipcode}')

        log.info('Step 3: cache more data in Redis')
        r.set('pam', 'pam@anywhere.com')
        r.set('fred', 'fred@fearless.com')

        log.info('Step 4: delete from cache')
        r.delete('andy')
        log.info(f'r.delete means andy is now: {email}')

        log.info(
            'Step 6: Redis can maintain a unique ID or count very efficiently')
        r.set('user_count', 21)
        r.incr('user_count')
        r.incr('user_count')
        r.decr('user_count')
        result = r.get('user_count')
        log.info('I could use this to generate unique ids')
        log.info(f'Redis says 21+1+1-1={result}')

        log.info('Step 7: richer data for a SKU')
        r.rpush('186675', 'chair')
        r.rpush('186675', 'red')
        r.rpush('186675', 'leather')
        r.rpush('186675', '5.99')

        log.info('Step 8: pull some data from the structure')
        cover_type = r.lindex('186675', 2)
        log.info(f'Type of cover = {cover_type}')

    except Exception as e:
        print(f'Redis error: {e}')
