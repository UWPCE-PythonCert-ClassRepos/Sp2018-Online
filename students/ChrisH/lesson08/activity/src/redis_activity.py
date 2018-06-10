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
        # r.set('andy', 'andy@somewhere.com')

        r.rpush('cust1', 'Albert', '206-555-1111', '98111')
        r.rpush('cust2', 'Bill', '206-555-2222', '98222')
        r.rpush('cust3', 'Charlie', '206-555-3333', '98333')
        r.rpush('cust4', 'David', '206-555-4444', '98444')
        r.rpush('cust5', 'Edward', '206-555-5555', '98555')
        r.rpush('cust6', 'Frank', '206-555-6666', '98666')

        print(f"Length of list for a customer: {r.llen('cust4')}")
        print(f"DBSize: {r.dbsize()}")
        print(f"Cust4 name: {r.lindex('cust4', 0)}")
        print(f"Cust4 zip: {r.lindex('cust4', 2)}")
        print(f"Cust4 phone: {r.lindex('cust4', 1)}")

        r.flushdb()

    except Exception as e:
        print(f'Redis error: {e}')


if __name__ == "__main__":

    run_example()
