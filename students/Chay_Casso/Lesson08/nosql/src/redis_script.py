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

        log.info('Step 9: do the homework')
        r.rpush('0001', 'Mike')
        r.rpush('0001', '4255551212')
        r.rpush('0001', '98101')
        r.rpush('0002', 'Pam')
        r.rpush('0002', '2065551212')
        r.rpush('0002', '98115')
        r.rpush('0003', 'Richard')
        r.rpush('0003', '2065559000')
        r.rpush('0003', '98104')
        r.rpush('0004', 'Slim')
        r.rpush('0004', '4255552912')
        r.rpush('0004', '98125')
        r.rpush('0005', 'Roger')
        r.rpush('0005', '3205557774')
        r.rpush('0005', '98122')
        r.rpush('0006', 'Stephen')
        r.rpush('0006', '2065551979')
        r.rpush('0006', '90210')

        log.info('Pull all information for a given user.')
        name = r.lindex('0004', 0)
        phone = r.lindex('0004', 1)
        zip = r.lindex('0004', 2)
        log.info(f'{name} has phone number {phone} and lives in {zip}.')

    except Exception as e:
        print(f'Redis error: {e}')
