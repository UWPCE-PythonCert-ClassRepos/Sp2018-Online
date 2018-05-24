"""
Generate mailroom report 
"""

from peewee import *
import logging
from mailroom.donor_donation_model import Donor, Donation
from mailroom.populate_donor_db import populate_db as pop_donor_db
from mailroom.populate_donation_db import populate_db as pop_donation_db
import mailroom.oo_mailroom as oo_mr

# only run this code if you haven't already created and populated the donor database
pop_donor_db()
pop_donation_db()

### Set up database
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('donor_donation.db')

logger.info('Working with Donor and Donation class')

logger.info('We join Donors to Donations')

# Create a query of donors with donations
try:
	database.connect()
	database.execute_sql('PRAGMA foreign_keys = ON;')
	query = (Donor
		.select(Donor, Donation)
		.join(Donation, JOIN.INNER)
		)

	logger.info('View records in the joined donor table')
	for donor in query:
		logger.info(f'\nDonor: {donor.donor_name}' + \
			f'\nDonor job: {donor.donor_occupation}' +\
			f'\nDonation amount: {donor.donation.donation_amount}')

	logger.info('Create DonorList object and populate it with' + \
		' Objects of class Donor')
	donor_list = oo_mr.DonorList()
	for donor in query:
		donor_to_add = oo_mr.Donor(donor.donor_name)
		for donations in query.where(donor.donor_name == donor_to_add.name):
			donor_to_add.add_donation(donor.donation.donation_amount)
		print(donor_to_add.name)
		print(donor_to_add.total_donations)
		print(donor_to_add.number_of_donations)
		donor_list.add_donor(donor_to_add)

except Exception as e:
	logger.info(e)

finally:
	logger.info('database closes')
	database.close()

donor_list.create_a_report()



