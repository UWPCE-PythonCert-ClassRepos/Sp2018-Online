#!/usr/bin/env python3

# -------------------------------------------------#
# Title: redis_donor.py
# Dev: Scott Luse
# Comments: I'm uncertain how to continue with Redis,
# my understanding of data storage is not clear on
# how to store multiple donations for a single person
# and then retrieve the data for reporting
# -------------------------------------------------#

import pprint
import login_database
import utilities

log = utilities.configure_logger('default', '../logs/redis_donor.log')


def donor_create_update(gift_amount, donor_name):
    """
    Redis add donor record
    uses non-presistent Redis only (as a cache)
    """
    try:
        log.info('Login to Redis')
        r = login_database.login_redis_cloud()
        r.set(donor_name, gift_amount)

        donation = r.get(donor_name)
        log.info("Donation from: " + donor_name)
        log.info(f'Donation amount confirmed: {donation}')

    except Exception as e:
        print(f'Redis error: {e}')

def donor_screen_report():
    """
    redis screen reporting
    """


def donor_delete_entry(gift_amount, donor_name):
    """
    redis delete single entry
    """
