"""
    Object Oriented Mail Room with Database
"""

import sqlite3
import logging
import pandas as pd
from peewee import *

from mailroom_OO_model import Donors, Donations
from mailroom_OO_initialize_data import populate_donors_db, populate_donations_db


class Donor(object):

    def __init__(self, name, donation):
        self.name = name
        self.donation = donation
        self.total = 0.00


class DonorList(object):

    def __init__(self):
        self.donor_list = {}

    def populate(self):
        populate_donors_db()
        populate_donations_db()

        conn = sqlite3.connect("mailroom.db")
        df_donors = pd.read_sql_query("select * from Donors;", conn)
        df_donations = pd.read_sql_query("select * from Donations;", conn)

        keys = df_donors[0].tolist()
        values = df_donations[0].tolist()
        self.donor_list = dict(zip(keys, values))

    def add_donor(self, donor):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        database = SqliteDatabase('mailroom.db')

        if donor.name in self.donor_list.keys():
            print("Donor already exists:  {}".format(donor))
            self.donor_list[donor.name].append(donor.donation)
            print("Donation Added to existing Donor")

            try:
                database.connect()
                database.execute_sql('PRAGMA foreign_keys = ON;')

                list_keys = list(self.donor_list.keys())
                last_key = list_keys[-1]

                list_values = list(self.donor_list.values())
                last_value = list_values[-1]

                with database.transaction():
                    new_donation = Donations.create(
                        donation_amount=last_value,
                        donation_donor_name=last_key)
                    new_donation.save()
                    logger.info('Database add successful')

                logger.info('Just saved a donation of {} from {} to the database'.format(last_value, last_key))

            except Exception as e:
                logger.info(f'Error creating = {last_key}')
                logger.info(e)

            finally:
                logger.info('database closes')
                database.close()

        else:
            self.donor_list[donor.name] = donor.donation

            try:
                database.connect()
                database.execute_sql('PRAGMA foreign_keys = ON;')

                list_keys = list(self.donor_list.keys())
                last_key = list_keys[-1]

                list_values = list(self.donor_list.values())
                last_value = list_values[-1]

                with database.transaction():
                    new_donor = Donors.create(
                        donor_name=last_key)
                    new_donor.save()
                    logger.info('Database donor add successful')

                with database.transaction():
                    new_donation = Donations.create(
                        donation_amount=last_value,
                        donation_donor_name=last_key)
                    new_donation.save()
                    logger.info('Database donation add successful')

                logger.info('Just saved a donation of {} from {} to the database'.format(last_value, last_key))

            except Exception as e:
                logger.info(f'Error creating = {last_key}')
                logger.info(e)

            finally:
                logger.info('database closes')
                database.close()

    def print_donors(self):
        print(self.donor_list)

    def thank_you(self):
        '''
        Sends a Thank You: Asks for a full name, Lists the donors, Asks for donation amount,
        Converts the donation to an integer, Adds donation amount to associated donor in list
        '''

        while True:
            input_key = input("Please enter a Full Name or type 'list' to see a list of donors: ")
            if input_key == 'list':
                print("\nHere is a list of the current donors:\n")
                for key, val in self.donor_list.items():
                    print(f"{key:20} $  {val}")

            elif input_key in self.donor_list.keys():
                while True:
                    try:
                        input_value = float(input("Enter a donation amount for {} : ".format(input_key)))
                    except ValueError as e:
                        print("Exception occurs in donation amount entered: {} \n".format(e))
                        continue
                    else:
                        self.donor_list[input_key].append(input_value)
                        print("\nDear {},\n\nThank You for the generous donation of ${}."
                              "\n\nThe Donation Center :^)".format(input_key, input_value))
                        break

            elif input_key not in self.donor_list.keys():
                while True:
                    try:
                        input_value = float(input("Enter a donation amount for {} : ".format(input_key)))
                    except ValueError as e:
                        print("Exception occurs in donation amount entered: {} \n".format(e))
                        continue
                    else:
                        self.donor_list[input_key] = [input_value]
                        print("\nDear {},\n\nThank You for the generous donation of ${}."
                              "\n\nThe Donation Center :^)".format(input_key, input_value))
                        break
            break

    def report(self):
        """ Prints a report with the Donor Name, Total Given, Number of Gifts, and Average Gift. """
        print("Donor Name                | Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------------")
        for key, val in self.donor_list.items():
            print(f"{key:25} $ {float(sum(val)):>12.2f}  {len(val):>8}  $ {float(sum(val))/len(val):>11.2f}")

    def letters(self):
        for key, val in self.donor_list.items():
            file = open('{}.txt'.format(key), 'w')
            with open('{}.txt'.format(key), 'w') as f:
                f.write("Dear {},\n\nThank You for donating a total of ${}. We look forward to hearing from you again."
                        "\n\nThe Donation Center ;^)".format(key, sum(val)))
            file.close()
        print("\n*** Text files have been created ***\n")


def menu():
    ''' Creates the user selection menu '''
    while True:
        print("\nPlease select an option:")
        print("1. Send a Thank You   |   2. Create a Report   |   3. Send letters to everyone   |   4. Quit")
        try:
            menu_selection = int(input())
        except ValueError as e:
            print("Exception occurs in menu_selection: {}".format(e))
            break
        else:
            return menu_selection


if __name__ == '__main__':

    dl = DonorList()
#   dl.populate()        tried populating the database but the method did not work

    while True:
        choice = menu()
        if choice == 1:
            dl.thank_you()
        elif choice == 2:
            dl.report()
        elif choice == 3:
            dl.letters()
        elif choice == 4:
            print("\n***\nYou have chosen to Exit the program. Goodbye!\n***")
            quit(4)
