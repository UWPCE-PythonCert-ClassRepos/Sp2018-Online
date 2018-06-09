#!/usr/bin/env python3
"""
    demonstrate use of Redis
    lesson 8 activity
    Add some customer data to the cache, Have Redis store a customer name,
    telephone and zip for 6 or so customers.
    Then show how you can retrieve a zip code,
    and then a phone number, for a known customer.
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

        log.info('lesson8 additions')
        r.rpush('jeff', 'jeff@jeff.com')
        r.rpush('jeff', '111-1111')
        r.rpush('jeff', '98888')
        r.rpush('mick', 'mick@mick.com')
        r.rpush('mick', '222-2222')
        r.rpush('mick', '77777')
        r.rpush('john', 'john@john.com')
        r.rpush('john', '333-3333')
        r.rpush('john', '55555')
        r.rpush('jintana', 'tangsuck@tangsuk.com')
        r.rpush('jintana', '444-4444')
        r.rpush('jintana', '88888')
        r.rpush('Thanh', 'thanh@thanh.com')
        r.rpush('Thanh', '555-5555')
        r.rpush('Thanh', '77755')

        log.info('Get johns Zip code')
        zip_code = r.lindex('john', 2)
        log.info(f'Johns ZipCode is {zip_code}')

        log.info('get Thanhs phone number')
        phone_number = r.lindex('Thanh', 1)
        log.info(f'Thanhs phone number is {phone_number}')

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
