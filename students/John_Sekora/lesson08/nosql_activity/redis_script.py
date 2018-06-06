"""
    demonstrate use of Redis
"""


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

        log.info('Step 3: cache more data in Redis')
        r.set('pam', 'pam@anywhere.com')
        r.set('fred', 'fred@fearless.com')

        # Add some mode customer data to the cache. (customer name, telephone, zip code)
        log.info('Update: Add some more customer data to Redis')
        r.set('Adam', '555-121-1000', '98204')
        r.set('Bill', '555-121-1340', '98204')
        r.set('Camile', '555-121-1067', '98223')
        r.set('David', '555-121-2300', '98212')
        r.set('Eugene', '555-121-3000', '95604')
        r.set('Frito', '555-121-1530', '98674')
        r.set('Greg', '555-121-8400', '98321')
        r.set('Harold', '555-121-1250', '96704')

        # Retrieve a zip code and phone number for a known customer
        log.info('Retrieving a zip code and phone number for a known customer')
        print(f'Results for David...  Telephone Number: {r.lindex("David", 0)}   Zip Code:{r.lindex("David", 1)}')

        log.info('Step 4: delete from cache')
        r.delete('andy')
        log.info(f'r.delete means andy is now: {email}')

        log.info('Step 6: Redis can maintain a unique ID or count very efficiently')
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
