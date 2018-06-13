"""
    demonstrate use of Redis
"""


import login_database
import utilities

"""
Create some data (at least 10 rows with about 5 fields 
in each). Show how you can read and write data in that format.
"""


def run_example():
    """
        uses non-presistent Redis only (as a cache)

    """

    log = utilities.configure_logger('default', '../logs/redis_script_persist.log')

    try:
        log.info('Step 1: connect to Redis')
        r = login_database.login_redis_cloud()
        log.info('Step 2: cache some data in Redis')
        r.set('test', 'TestDBWrite')

        log.info('Step 3: now I can read it')
        test = r.get('test')
        log.info('But I must know the key')
        log.info(f'The results of r.get: {test}')

        log.info('Step 4: cache more data in Redis')
        r.set('customer1_name','Bob Smith')
        r.set('customer1_phone', '555-555-5555')
        r.set('customer1_zip', '98103')
        r.set('customer1_city', 'Seattle')
        r.set('customer1_state', 'WA')
        r.set('customer2_name', 'Flash Gordon')
        r.set('customer2_phone', '555-555-5555')
        r.set('customer2_zip', '78671')
        r.set('customer2_city', 'San Francisco')
        r.set('customer2_state', 'CA')
        r.set('customer3_name', 'Pickle Rick')
        r.set('customer3_phone', '210-676-5555')
        r.set('customer3_zip', '98103')
        r.set('customer3_city', 'Oakland')
        r.set('customer3_state', 'CA')
        r.set('customer4_name', 'Lana Kane')
        r.set('customer4_phone', '555-333-8989')
        r.set('customer4_zip', '49813')
        r.set('customer4_city', 'Gotham')
        r.set('customer4_state', 'DI')
        r.set('customer5_name', 'Bob Belcher')
        r.set('customer5_phone', '206-555-5555')
        r.set('customer5_zip', '38791')
        r.set('customer5_city', 'Olympia')
        r.set('customer5_state', 'WA')
        r.set('customer6_name', 'Lisa Simpson')
        r.set('customer6_phone', '555-555-5555')
        r.set('customer6_zip', '91728')
        r.set('customer6_city', 'Seattle')
        r.set('customer6_state', 'WA')
        r.set('customer7_name', 'Waylon Jennings')
        r.set('customer7_phone', '555-555-6666')
        r.set('customer7_zip', '98120')
        r.set('customer7_city', 'Portland')
        r.set('customer7_state', 'OR')
        r.set('customer8_name', 'Bob Jennings')
        r.set('customer8_phone', '555-555-6666')
        r.set('customer8_zip', '98120')
        r.set('customer8_city', 'Portland')
        r.set('customer8_state', 'OR')
        r.set('customer9_name', 'Peter Parker')
        r.set('customer9_phone', '555-555-6666')
        r.set('customer9_zip', '21289')
        r.set('customer9_city', 'New York')
        r.set('customer9_state', 'NY')
        r.set('customer10_name', 'James Rockford')
        r.set('customer10_phone', '555-555-9999')
        r.set('customer10_zip', '12345')
        r.set('customer10_city', 'Malibu')
        r.set('customer10_state', 'CA')

        log.info('Step 5: retrieve some customer info')
        cust1_name = r.get('customer1_name')
        log.info(f'Customer 1 name is: {cust1_name}')
        cust3_phone = r.get('customer3_phone')
        log.info(f'Customer 3 has phone number: {cust3_phone}')
        cust5_zip = r.get('customer5_zip')
        log.info(f'The zip code for Customer 5 is: {cust5_zip}')
        cust3_name = r.get('customer3_name')
        log.info(f'Customer 3 name is: {cust3_name}')
        cust10_name = r.get('customer10_name')
        log.info(f'{cust10_name} is the GOAT')

        log.info(
            'Step 7: Redis can maintain a unique ID or count very efficiently')
        r.set('user_count', 21)
        r.incr('user_count')
        r.incr('user_count')
        r.decr('user_count')
        result = r.get('user_count')
        log.info('I could use this to generate unique ids')
        log.info(f'Redis says 21+1+1-1={result}')

        log.info('Step 8: richer data for a SKU')
        r.rpush('186675', 'chair')
        r.rpush('186675', 'red')
        r.rpush('186675', 'leather')
        r.rpush('186675', '5.99')

        log.info('Step 9: pull some data from the structure')
        cover_type = r.lindex('186675', 2)
        log.info(f'Type of cover = {cover_type}')

        log.info('Step 10: working with redis as a list')
        r.lpush('Angel', *['Rocky', 'Rockfish', 'Dennis'])

        redis_test = r.lindex('Angel', 1)
        log.info(f'Data should be Rockfish - {redis_test}')

    except Exception as e:
        print(f'Redis error: {e}')

if __name__ == '__main__':
    """
    redis persistence example
    """

    run_example()