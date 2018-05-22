#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom menu
# Dev: Scott Luse
# Date: 05/20/2018
# -------------------------------------------------#

'''
mailroom menu for interacting with user
'''

import sys
import logging
from peewee import *
from mroom_model import Donor, Gift
from datetime import date
import time

def add_donor(don_name, address="None", town="None"):
    """"
    Add a new donor to the donor database

    :param: the name of the donor

    :returns:
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('donor.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Add and display a new donor name...')

        new_person = Donor.create(
            donor_name = don_name,
            home_address = address,
            town_and_zip = town)
        new_person.save()

        logger.info('Show new donor name')
        aperson = Donor.get(Donor.donor_name == don_name)

        logger.info(f'We just created {aperson.donor_name}')
        logger.info(f'Who lives at {aperson.home_address}, in the town {aperson.town_and_zip}')
        logger.info('Reading and print all Donor records...')

        for person in Donor:
            logger.info(
                f"{person.donor_name} lives at {person.home_address} in the town {person.town_and_zip}")

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def delete_donor(don_name):
    """"
    Delete donor from the donor database

    :param: the name of the donor

    :returns:
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('donor.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Display the donor and then delete him...')
        aperson = Donor.get(Donor.donor_name == don_name)

        # Add error check for SQL record not found

        logger.info(f'We just found {aperson.donor_name}')
        logger.info(f'Who lives at {aperson.home_address}, in the town {aperson.town_and_zip}')
        logger.info('and now we will delete the donor...')

        # Delete and Gift Records too for data integrity?

        aperson.delete_instance()
        logger.info('Reading and print all Person records for confirmation...')

        for person in Donor:
            logger.info(
                f"{person.donor_name} lives at {person.home_address} in the town {person.town_and_zip}")

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def update_donor_address(address, don_name):
    """"
    Update the donor address

    :param: new address, name of donor

    :returns:
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('donor.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Display the donor and then delete him...')
        aperson = Donor.get(Donor.donor_name == don_name)

        # Add error check for SQL record not found

        logger.info(f'We just found {aperson.donor_name}')
        logger.info(f'Who lives at {aperson.home_address}, in the town {aperson.town_and_zip}')
        logger.info('and now we will update donor ADDRESS...')

        aperson.home_address = address
        aperson.save()

        logger.info('Reading and print all Person records for confirmation...')

        for person in Donor:
            logger.info(
                f"{person.donor_name} lives at {person.home_address} in the town {person.town_and_zip}")

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def create_gift_record(amount, don_name):
    """"
    Create new donation Gift record

    :param: amount, name of donor

    :returns:
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('donor.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Creating gift record with associated Donor name...')
        now = date.today()
        theday = str(now.month) + "-" + str(now.day) + "-" + str(now.year)

        new_gift = Gift.create(
            gift_key = don_name + theday + time.strftime("%H:%M:%S"),
            gift_date = theday,
            gift_amount = amount,
            donor_name = don_name)
        new_gift.save()

        for gift in Gift:
            logger.info(f'Key {gift.gift_key} on date {gift.gift_date}')
            logger.info(f'for amount {gift.gift_amount} from {gift.donor_name}')

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def screen_report():
    """"
    Display donation giving report on screen

    :param:

    :returns:
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('donor.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Reading and print all Person records for confirmation...')

        for person in Donor:
            logger.info(
                f"{person.donor_name} lives at {person.home_address} in the town {person.town_and_zip}")

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def donor_name_input(option):
    name = input("Please enter donor NAME or 'main' for the menu: ")
    if name.lower() == "main":
        return
    else:
        process_name(option, name)


def donor_address_input(name):
    address = input("Please enter donor ADRESS or 'main' for the menu: ")
    if address.lower() == "main":
        return
    else:
        update_donor_address(address, name)


def add_gift(name):
    amount = input("Please enter donation AMOUNT or 'main' for the menu: ")
    if amount.lower() == "main":
        return
    else:
        create_gift_record(amount, name)


def process_name(option, name):
    if option == '1':
        add_donor(name)
    elif option == '2':
        delete_donor(name)
    elif option == '3':
        donor_address_input(name)
    elif option == '4':
        add_gift(name)


def get_user_choice():
    '''
    Create main menu selection
    '''
    print("""
    MailRoom SQL Programming Menu Options
    1) Add Donor Name To Database
    2) Delete Donor Name to Database
    3) Update Donor Mailing Address
    4) Add Financial Gift ($)
    5) Create Screen Report
    6) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 6]: ")
    return (user_choice.strip())

def process_menu(menu_item):
    if menu_item == '1':
        donor_name_input("1")
    elif menu_item == '2':
        donor_name_input("2")
    elif menu_item == '3':
        donor_name_input("3")
    elif menu_item == '4':
        donor_name_input("4")
    elif menu_item == '5':
        screen_report()

def quit():
    sys.exit(0)

def main():
    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "6":
            print("Goodbye!")
            quit()
        else:
            process_menu(get_user_action)

if __name__ == '__main__':
    main()
