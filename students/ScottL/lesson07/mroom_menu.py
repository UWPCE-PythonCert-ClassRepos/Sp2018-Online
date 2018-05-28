#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom menu
# Dev: Scott Luse
# Date: 05/21/2018
# -------------------------------------------------#

'''
mailroom menu for interacting with user
Known Issues:
1. Deleting donor records is not working, I'm still trying to
delete associated gift records to maintain db integrity
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

    # Add valid number check for gift amount
    first_gift = input("Please enter donation AMOUNT or 'main' for the menu: ")
    if first_gift.lower() == "main":
        return
    else:
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


        except Exception as e:
            logger.info(e)

        finally:
            database.close()
            create_gift_record(first_gift, don_name)


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

        aperson = Donor.get(Donor.donor_name == don_name)
        # Add error check for SQL record not found

        # aperson.delete_instance()
        print('WARNING: Donor record not deleted to keep database integrity')

        # Need Pythonic method for deleting donation records
        # database.execute('DELETE FROM Gift WHERE donor_name = don_name')

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

        aperson = Donor.get(Donor.donor_name == don_name)

        # Add error check for SQL record not found

        aperson.home_address = address
        aperson.save()

        print(f"{aperson.donor_name} now lives at {aperson.home_address}!")

    except Exception as e:
        logger.info(e)

    finally:
        database.close()


def create_gift_record(amount, don_name):
    """"
    Create new donation Gift record
    gift_key uses 'name+date+time' for unique value

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
        key_name = don_name.replace(" ", "")

        new_gift = Gift.create(
            gift_key = key_name + theday + time.strftime("%H:%M:%S"),
            gift_date = theday,
            gift_amount = amount,
            donor_name = don_name)
        new_gift.save()

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

        '''
        # test code for listing all donation records
        query_test = (Donor
                 .select(Donor, Gift)
                 .join(Gift, JOIN.INNER)
                )
        for donor in query_test:
            print(f'{donor.donor_name} gave {donor.gift.gift_amount} on {donor.gift.gift_key}')
        '''

        query_sum = (Donor
                 .select(Donor, fn.SUM(Gift.gift_amount).alias('gift_totals'),
                         fn.COUNT(Gift.gift_amount).alias('gift_count'))
                 .join(Gift, JOIN.LEFT_OUTER)
                 .group_by(Donor)
                 .order_by(Donor.donor_name))

        '''
        # test code for showing donation total values
        for donor in query_sum:
            print(f'{donor.donor_name} gave {donor.gift_totals} dollars')
        '''

        print('')
        print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name (SQL)', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
        print('-' * 55)
        for donor in query_sum:
            name = donor.donor_name
            num_gifts = donor.gift_count
            total_gifts = "{:.2f}".format(donor.gift_totals)
            avg_gift = "{:.2f}".format(donor.gift_totals/donor.gift_count)

            print('{:20}{:>15}{:>10}{:>10}'.format(name, total_gifts, num_gifts, avg_gift))

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
    2) Delete Donor Record & Donations!
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
