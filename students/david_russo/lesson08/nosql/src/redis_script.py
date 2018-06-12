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
        r.rpush('0001', 'andy', '123-456-4444', '12345')
        r.rpush('0002', 'brad', '123-456-5555', '23456')
        r.rpush('0003', 'cory', '123-456-6666', '34567')
        r.rpush('0004', 'diane', '123-456-7777', '45678')
        r.rpush('0005', 'ellen', '123-456-8888', '56789')
        r.rpush('0006', 'felicity', '123-456-9999'. '67891')

        # log.info('Step 2: now I can read it')
        # email = r.get('andy')
        # log.info('But I must know the key')
        # log.info(f'The results of r.get: {email}')

        # log.info('Step 3: cache more data in Redis')
        # r.set('pam', 'pam@anywhere.com')
        # r.set('fred', 'fred@fearless.com')

        # log.info('Step 4: delete from cache')
        # r.delete('andy')
        # log.info(f'r.delete means andy is now: {email}')

        # log.info(
        #     'Step 6: Redis can maintain a unique ID or count very efficiently')
        # r.set('user_count', 21)
        # r.incr('user_count')
        # r.incr('user_count')
        # r.decr('user_count')
        # result = r.get('user_count')
        # log.info('I could use this to generate unique ids')
        # log.info(f'Redis says 21+1+1-1={result}')

        # log.info('Step 7: richer data for a SKU')
        # r.rpush('186675', 'chair')
        # r.rpush('186675', 'red')
        # r.rpush('186675', 'leather')
        # r.rpush('186675', '5.99')

        # log.info('Step 8: pull some data from the structure')
        # cover_type = r.lindex('186675', 2)
        # log.info(f'Type of cover = {cover_type}')

        log.info('Step 2: Retrieve data for cust 0006')
        log.info(f'Zip code for cust 0006: {r.lindex('0006', 2)}')
        log.info(f'Phone number for cust 0006: {r.lindex('0006', 1)}')


    except Exception as e:
        print(f'Redis error: {e}')
