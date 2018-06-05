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
		.select(Donor, Donation,
		fn.Sum(Donation.donation_amount).alias('total_donations'),
		fn.Count(Donor.donor_name).alias('num_gifts'),
		fn.Avg(Donation.donation_amount).alias('mean_gift_size'))
		.join(Donation, JOIN.INNER)
		.group_by(Donor.donor_name))

except Exception as e:
	logger.info(e)

finally:
	logger.info('database closes')
	database.close()

for donor in query:
	print(f'Donor: {donor.donor_name}\t' + \
		  f'Total Donations: {donor.total_donations}\t' + \
		  f'Number of Donations: {donor.num_gifts}\t' + \
		  f'Average gift size: {donor.mean_gift_size}\t')



