

import login_database
# import logging

def get_donors():
    donors = [
        {

            'first_name': 'Frank',
            'last_name': 'Lampard',
            'age': 43
        },
        {
            'first_name': 'Mary',
            'last_name': 'Smith',
            'age': 23
        }

    ]

    return donors

def seed_mailroom():
    with login_database.login_mongodb_cloud() as client:
        db = client['mailroom']
        db.insert_many(get_donors())


if __name__ == '__main__':
    seed_mailroom()


#
#
#
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# database = SqliteDatabase('../data/mailroom.db')
#
#
# def add_donors():
#     donors = [
#         ('Andrew', 'Smith', 'Leeds'),
#         ('Peter', 'Pan', 'Neverland'),
#         ('Susan', 'Smith', 'Andover'),
#         ('Pam', 'Feank', 'Coventry'),
#         ('Steven', 'King', 'Colchester'),
#     ]
#
#     donor_first_name = 0
#     donor_last_name = 1
#     donor_city = 2
#
#     try:
#
#         for donor in donors:
#             with database.transaction():
#                 new_donor = Donor.create(
#                     first_name=donor[donor_first_name],
#                     last_name=donor[donor_last_name],
#                     city=donor[donor_city]
#                 )
#                 new_donor.save()
#         logger.info('Added Donors.....')
#
#         logger.info('Print the Person records we saved...')
#         for saved_donor in Donor:
#             logger.info(f'{saved_donor.donor_first_name} lives in {saved_donor.donor_city} ')
#
#     except Exception as e:
#         logger.info(f'Error creating = {donor[donor_first_name]}')
#         logger.info(e)
#         logger.info('See how the database protects our data')
#
# def add_donations():
#     donations = [
#         (100,'Andrew'),
#         (101,'Andrew'),
#         (102,'Andrew'),
#         (10,'Peter'),
#         (20,'Peter'),
#         (30,'Peter'),
#         (50000,'Susan'),
#         (40000,'Susan'),
#         (3000,'Susan'),
#         (500,'Pam'),
#         (200,'Pam'),
#         (25,'Steven'),
#     ]
#
#     donation_amount = 0
#     donor = 1
#
#     try:
#         for donation in donations:
#             with database.transaction():
#                 new_donation = Donation.create(
#                     amount=donation[donation_amount],
#                     donor=donation[donor]
#                 )
#                 new_donation.save()
#         logger.info('Added Donations.....')
#
#         logger.info('Print the Person records we saved...')
#         for saved_donation in Donation:
#             logger.info(f'{saved_donation.donor} donated  {saved_donation.donation_amount} ')
#
#     except Exception as e:
#         logger.info(f'Error creating = {donation[donation_amount]}, for {donation[donor]}')
#         logger.info(e)
#         logger.info('See how the database protects our data')
#
# def drop_tables():
#     pass
#     # if database.get_tables():
#     #     for table in database.get_tables():
#
#
# # if __name__ == '__main__':
# #     # database.connect()
# #     # database.execute_sql('PRAGMA foreign_keys = ON;')
# #     # drop_tables()
# #     # add_donors()
# #     # add_donations()
#     # database.close()