
import logging
from peewee import *
from mailroom_model import Donor, Donation
import random
from uuid import uuid4
from datetime import date
import pprint


def display_donor():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    logger.info('Printing Donor with donations given')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Donor
                 .select(Donor, fn.SUM(Donation.amount).alias('dsum'))
                 .join(Donation, JOIN.LEFT_OUTER)
                 .group_by(Donor.last_name)
                 )

        logger.info('View matching records from all tables')
        for d in query:
            print(f'Donor {d.first_name}, {d.last_name} gave a total of ${d.dsum:^,.2f}')

    except Exception as e:
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def add_donor():
    """
        Add a new donor to the donor database

    """
    # Create variables to provide random 3 digit id for Donor primary key
    x = random.randrange(1, 9)
    y = random.randrange(1, 9)
    z = random.randrange(1, 9)
    value = str(x) + str(y) + str(z)

    pri_ID = int(value) # will be inserted as first value of new record for Donor and Donation
    donor = [] # Used to hold user input

    first_name = 0
    last_name = 1
    state = 2
    job_type = 3

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    while True:
        record = input("""
                       Enter donor data in the following format:
                       'First Name, Last Name, State, Job Type'
                       ex: Samuel, Jackson, NY, Actor
                       Type quit - to exit to main menu.
                       Enter input here >>  """)
        if 'quit' in record.lower():
            break
        else:
            for data in record.split(','):
                donor.append(data)

            logger.info('Connecting to database....')
            database = SqliteDatabase('donor.db')
            try:
                database.connect()
                database.execute_sql('PRAGMA foreign_keys = ON;')

                logger.info('Add and display a new donor name...')
                new_person = Donor.create(
                    donor_ID=pri_ID,
                    first_name=donor[first_name],
                    last_name=donor[last_name],
                    state=donor[state],
                    job_type=donor[job_type],
                )
                new_person.save()
                logger.info('Show new donor name')
                a_person = Donor.get(Donor.donor_ID == pri_ID)
                logger.info(f'We just created {a_person.first_name}, {a_person.last_name}')

            except Exception as e:
                logger.info(e)

            finally:
                database.close()

def add_donation(pri_key):
    # Create variables to provide random 3 digit id for Donor primary key
    x = random.randrange(1, 9)
    y = random.randrange(1, 9)
    z = random.randrange(1, 9)
    value = str(x) + str(y) + str(z)

    pri_id = int(value)  # will be inserted as first value of new record for Donor and Donation

    now = str(date.today())

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    while True:
        amount = input("""
                           Enter donation amount and any notes in the following format:
                           '0.00, ex: 200.50                          
                           Enter input here >>  """)
        notes = input("Enter any notes for donation >> ")

        try:
            logger.info('Adding donation...')
            new_person = Donation.create(
                money_ID=pri_id,
                donor_ID=pri_key,
                amount="%.2f" % amount,
                date=now,
                notes=notes,
            )
            new_person.save()
            logger.info('Show new donor name')
            a_donation = Donation.get(Donation.money_ID == pri_id)
            logger.info(f'We just created new record with ID: {a_donation.money_ID}')

        except Exception as e:
            logger.info(e)

        finally:
            break


def del_donor():
    pass


def update_donor():
    pass


def quit_menu():
    print("Shutting down program, Goodbye", end='\n')
    return "exit menu"


def user_selection(user_prompt, queue_dict):
    # Runs until user inputs 'q'
    while True:
        # Make sure all Key values are capitalized
        response = input(user_prompt)
        if queue_dict[response]() == "exit menu":
            break


def main():
    user_prompt = ("\n\nWelcome to the MailRoom Donar Program!\n"
                   "What would you like to do?\n"
                   "Type '1- To Add donor'\n"
                   "Type '2- To Delete a donor'\n"
                   "Type '3- To Update a donor'\n"
                   "Type '4- To Display a donor'\n"
                   "Type 'q- To end the program'\n"
                   "Enter value here >> ")
    """
    Use dictionary to create quasi switch/case structure
    """
    menu_dict = {"1": display_donor,
                 "2": add_donor,
                 "3": update_donor,
                 "4": del_donor,
                 "q": quit_menu}
    # Pass the user_prompt and menu_dict to the user_selection function
    user_selection(user_prompt, menu_dict)


def initial_data_load():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')
    logger.info('Working with Donor class')
    logger.info('Creating a record in Donor and Donation')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        user = Donor.create(donor_ID=999, first_name='Samuel', last_name='Jackson', state='NY', job_type='Actor')
        user.save()
        logger.info('Database add successful ')

    except Exception as e:
        logger.info(f'Error creating = {user.donor_ID}')
        logger.info(e)

    finally:
        logger.info('Printing records in the Donor table')
        for p in Donor.select():
            logger.info(f'Created Record Name: {p.first_name}, {p.last_name} with id: {p.donor_ID}')

        logger.info('database closes')
        database.close()

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        dollar = Donation.create(money_ID=999, donor_ID=999, amount=1400, date=str(date.today()), notes='')
        dollar.save()
        # Donation.create(money_ID=uuid4(), donor_ID=money, amount=1400.50, date=now, notes='Hope this works')

    except Exception as e:
        logger.info(f'Error creating = {dollar.money_ID}')
        logger.info(e)

    finally:
        logger.info('Printing records in the Donation table')
        for d in Donation.select():
            logger.info(f'Created Record: {d.money_ID}, {d.donor_ID}, with amount {d.amount}')

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
    main()