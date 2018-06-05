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
        #r.set('andy', 'andy@somewhere.com')

        r.rpush('customer1', 'sirisha', '206-111-1111', '98111')
        r.rpush('customer2', 'jessy', '206-222-2222', '98129')
        r.rpush('customer3', 'david', '206-333-3333', '98127')
        r.rpush('customer4', 'sam', '425-111-2222', '98052')
        r.rpush('customer5', 'alex', '425-222-3333', '98007')
        r.rpush('customer6', 'bill', '425-333-4444', '98006')

        print(f"Length of list for customer1 is: {r.llen('customer1')}")
        print(f"Database size: {r.dbsize()}")
        print(f"customer1 name:{r.lindex('customer1', 0)}")
        print(f"customer1 telephone: {r.lindex('zip',1)}")
        print(f"customer1 zip: {r.lindex('customer1', 2)}")

    except Exception as e:
        print(f'Redis error: {e}')


if __name__ =="__main__":
    run_example()
