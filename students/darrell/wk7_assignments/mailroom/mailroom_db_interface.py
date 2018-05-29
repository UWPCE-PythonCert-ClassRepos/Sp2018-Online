import logging
from peewee import *
from mailroom_schema import Donor, Donation


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
database = SqliteDatabase('../data/mailroom.db')


def create_donor():
    pass

def get_all_donors():
    result =  Donor.select()
    return result

def get_all_donations():
    result = Donation.select()
    database.close()

def update_donor():
    pass

def delete_donor():
    pass

