
import logging
from peewee import *
from mailroom_model import Donor, Donation
from uuid import uuid4
from datetime import date

# Global date variable
#now = date.today().strftime("%y-%m-%d")

# def display_donor():
#     pass
#
# def add_donor():
#     """
#         Add a new donor to the donor database
#
#     """
#     donor = []
#     logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger(__name__)
#     # Add valid number check for gift amount
#     while True:
#         record = input("""
#                        Enter donor data in the following format:
#                        'First Name, Last Name, State, Job Type'
#                        ex: Samuel, Jackson, NY, Actor
#                        Type quit - to exit to main menu.
#                        Enter input here >>  """)
#         if 'quit' in record.lower():
#             break
#         else:
#             for data in record.split(','):
#                 donor.append(data)
#
#             logger.info('Connecting to database....')
#             database = SqliteDatabase('donor.db')
#             try:
#                 database.connect()
#                 database.execute_sql('PRAGMA foreign_keys = ON;')
#
#                 logger.info('Add and display a new donor name...')
#                 new_person = Donor.create(
#                     donor_name=don_name,
#                     home_address=address,
#                     town_and_zip=town)
#                 new_person.save()
#                 logger.info('Show new donor name')
#                 aperson = Donor.get(Donor.donor_name == don_name)
#                 logger.info(f'We just created {aperson.donor_name}')
#
#
#         except Exception as e:
#             logger.info(e)
#
#         finally:
#             database.close()
#             create_gift_record(first_gift, don_name)
#
#
# def del_donor():
#     pass
#
# def update_donor():
#     pass
#
# def quit_menu():
#     print("Shutting down program, Goodbye", end='\n')
#     return "exit menu"
#
#
# def user_selection(user_prompt, queue_dict):
#     # Runs until user inputs 'q'
#     while True:
#         # Make sure all Key values are capitalized
#         response = input(user_prompt)
#         if queue_dict[response]() == "exit menu":
#             break
#
#
# def main():
#     user_prompt = ("\n\nWelcome to the MailRoom Donar Program!\n"
#                    "What would you like to do?\n"
#                    "Type '1- To Add donor'\n"
#                    "Type '2- To Delete a donor'\n"
#                    "Type '3- To Update a donor'\n"
#                    "Type '4- To Display a donor'\n"
#                    "Type 'q- To end the program'\n"
#                    "Enter value here >> ")
#     """
#     Use dictionary to create quasi switch/case structure
#     """
#     menu_dict = {"1": display_donor,
#                  "2": add_donor,
#                  "3": update_donor,
#                  "4": del_donor,
#                  "q": quit_menu}
#     # Pass the user_prompt and menu_dict to the user_selection function
#     user_selection(user_prompt, menu_dict)


def initial_data_load():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')
    logger.info('Working with Donor class')
    logger.info('Creating a record in Donor and Donation')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        Donor.create(donor_ID=999, first_name='Samuel', last_name='Jackson', state='NY', job_type='Actor')

    except Exception as e:
        logger.info(f'Error creating = {Donor.donor_ID}')
        logger.info(e)

    finally:
        logger.info('Printing records in the Donor table')
        for p in Donor.select():
            logger.info(f'Created Record Name: {p.first_name}, {p.last_name} with random id: {p.donor_ID}')

        logger.info('database closes')
        database.close()

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        Donation.create(money_ID=999, donor_ID=999, amount=1400, date=str(date.today()), notes='')
        # Donation.create(money_ID=uuid4(), donor_ID=money, amount=1400.50, date=now, notes='Hope this works')

    except Exception as e:
        logger.info(f'Error creating = {Donation.money_ID}')
        logger.info(e)

    finally:
        logger.info('Printing records in the Donation table')
        for d in Donation.select():
            logger.info(f'Created Record: {d.money_ID}, {d.donor_ID}, with amount {d.amount} with random id: {d.date}')

        logger.info('database closes')
        database.close()


        # query = (Donor.select(Donor, Donation).join(Donation, JOIN.INNER))
        #
        # logger.info('View matching records from both tables')
        # for person in query:
        #     logger.info(f'Person {person.first_name}, {person.last_name} gave amount \
        #     {person.donation.amount}')

if __name__ == "__main__":
    initial_data_load()
    #main()