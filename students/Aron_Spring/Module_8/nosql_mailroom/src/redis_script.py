"""
    demonstrate use of Redis
"""


import login_database
import utilities

"""
Seed mailroom data to cache, read the cache for mailroom info
and update cache to include new entry

"""


def redis_mailroom():
    """
        uses non-presistent Redis only (as a cache).
        seeding data one at a time
    """

    log = utilities.configure_logger('default', '../logs/redis_script.log')

    try:
        log.info('Connect to Redis')
        r = login_database.login_redis_cloud()

        r.set('Donor_tjefferson', 'Thomas Jefferson')
        r.set('Email_tjefferson', 'thomasj@us.gov')
        r.set('Donation_tjefferson','100')
        r.set('Donor_brubble', 'Betty Rubble')
        r.set('Email_brubble', 'brubble@bedrock.com')
        r.set('Donation_brubble','500')
        r.set('Donor_gjetson', 'George Jetson')
        r.set('Email_gjetson', 'georgej@sprokets.com')
        r.set('Donation_gjetson','60')
        r.set('Donor_lsimpson', 'Lisa Simpson')
        r.set('Email_lsimpson', 'lsimpson@krusty.com')
        r.set('Donation_lsimpson','100')

        log.info('Retrieve some customer info')
        donor_name = r.get('Donor_brubble')
        log.info(f'Donor name is: {donor_name}')
        donor_email = r.get('Email_lsimpson')
        log.info(f'Lisa Simpson has email: {donor_email}')
        donation = r.get('Donation_gjetson')
        log.info(f'The initial donation by George Jetson: ${donation}')

    except Exception as e:
        print(f'Redis error: {e}')

def redis_mailroom_donor(name):
    """
    search for a donor by donor ID
    """
    log = utilities.configure_logger('default', '../logs/redis_script.log')

    try:
        log.info('Connect to Redis')
        r = login_database.login_redis_cloud()
        if r.exists(name) == True:
            return log.info(f'The donor ID {name} is present')
        else:
            return log.info(f'No such donor found')

    except Exception as e:
        print(f'Redis error: {e}')

def redis_mailroom_search(search):
    """
    search for all emails in the redis cache
    email would be 'Email*' for example
    """
    log = utilities.configure_logger('default', '../logs/redis_script.log')
    log.info('Connect to Redis')
    r = login_database.login_redis_cloud()

    list = r.keys(search)

    for num, email in enumerate(list):
        emails = r.get(email)
        print(emails)


