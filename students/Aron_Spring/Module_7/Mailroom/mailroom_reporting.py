import logging
from peewee import *
from Mailroom.mailroom_db_model import Donor, Donation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('mailroom.db')
logger.info('Reporting Donor and Donation records')

def list_donations():
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    result =''
    query = (Donation
             .select(Donation.donor_name, Donation.donation_amount, Donation.donation_date)
             .join(Donor)
            )
    for row in query.dicts():
        result += f"{row['donor_name']}"\
            f"{row['donation_amount']}"\
            f"${row['donation_date']}"\
            f"\n"
        return result
    database.close()

def list_donors():
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    result = ''
    query = (Donor
             .select(Donor.donor_name, Donor.donor_city, Donor.donor_nickname)
             )
    for row in query.dicts():
        result += f"{row['donor_name']}" \
                  f"{row['donor_city']}" \
                  f"${row['donor_nickname']}" \
                  f"\n"
        return result
    database.close()

def sum_donations():
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')
    query = Donor.select(Donor.donor_name,
                         fn.sum(Donation.donation_amount).alias('sum_donation')).join(Donation)\
                        .group_by(Donor.donor_name)
    result = ""
    for row in query.dicts():
        result += "{:10} ${:10.2f}\n".format(row['donor_name'],
                                           row['sum_donation'])

    return(f"{result}")
    database.close()