"""
    demonstrate use of Redis
"""


import login_database
import utilities


def run_example():
    """
        uses non-persistent Redis only (as a cache)

    """

    log = utilities.configure_logger('default', '../logs/redis_script.log')

    try:
        log.info('Step 1: connect to Redis')
        r = login_database.login_redis_cloud()

        log.info('Step 2: do the homework')
        r.rpush('William Gates III', 'bill.gates@msn.com')
        r.rpush('William Gates III', '4255551212')
        r.rpush('William Gates III', '98101')
        r.rpush('Jeff Bezos', 'bezos@amazon.com')
        r.rpush('Jeff Bezos', '2065551212')
        r.rpush('Jeff Bezos', '98115')
        r.rpush('Paul Allen', 'paul.allen@hotmail.com')
        r.rpush('Paul Allen', '2065559000')
        r.rpush('Paul Allen', '98104')
        r.rpush('Mark Zuckerberg', 'zuck@facebook.com')
        r.rpush('Mark Zuckerberg', '4255552912')
        r.rpush('Mark Zuckerberg', '98125')

    except Exception as e:
        print(f'Redis error: {e}')

if __name__ == '__main__':
    run_example()