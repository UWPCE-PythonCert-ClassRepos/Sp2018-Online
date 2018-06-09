#!/usr/bin/env python3
"""
Object-oriented Mailroom - Working with Relational Databases
"""
import logging
import os
import sys
import math
import peewee
from datetime import date
from textwrap import dedent

from create_donor_model import Donor as D
from create_donor_model import Donation

# Utility so we have data to test with, etc.
def get_sample_data():
    """
    returns a list of donor objects to use as sample data


    """
    return [Donor("Jimmy Nguyen", [653772.32, 12.17]),
            Donor("Steve Smith", [877.33]),
            Donor("Julia Norton", [877.33]),
            Donor("Ed Johnson", [663.23, 43.87, 1.32]),
            Donor("Elizabeth McBath", [1663.23, 4300.87, 10432.0]),
            ]

# Setup logging for mailroom
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Logging to console for Mailroom')


##################################################
#        Classes from Rick posted in Slack       #
##################################################
class Donor():
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donations=None):
        """
        create a new Donor object

        :param name: the full name of the donor

        :param donations=None: iterable of past donations
        """

        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key

        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip().replace(" ", "")

    @property
    def last_donation(self):
        """
        The most recent donation made
        """
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, amount):
        """
        add a new donation
        """
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Donation must be greater than zero")
        self.donations.append(amount)


class DonorDB():
    """
    encapsulation of the entire database of donors and data associated with them.
    """

    def __init__(self, donors=None):
        """
        Initialize a new donor database

        :param donors=None: iterable of Donor objects
        """
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    # def save_to_file(self, filename):
    #     with open(filename, 'w') as outfile:
    #         self.to_json(outfile)

    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as infile:
    #         obj = js.from_json(infile)
    #     return obj

    @property
    def donors(self):
        """
        an iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):
        """
        creates a list of the donors as a string, so they can be printed

        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db

        :param: the name of the donor

        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.normalize_name(name))

    def add_donor(self, name):
        """
        Add a new donor to the donor db

        :param: the name of the donor

        :returns: the new Donor data structure
        """
        donor = Donor(name)
        self.donor_data[donor.norm_name] = donor
        return donor

    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor

        :param: donor tuple

        :returns: string with letter

        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(donor.name, donor.last_donation)
                      )

    @staticmethod
    def sort_key(item):
        # used to sort on name in self.donor_data
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.

        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gift = donor.average_donation
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        for donor in self.donor_data.values():
            print("Writing a letter to:", donor.name)
            letter = self.gen_letter(donor)
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)


##################################################
# Working with the database for CRUD operations  #
##################################################
logger.info('Defining location of database file')
db_file = os.path.abspath('data/donormanagement.db')
donor_db = peewee.SqliteDatabase(db_file)

logger.info('functions to implement CRUD operations - Create, Retrieve, Update, Delete')


def create_donor_record(donor_name, donor_city=None):
    """Function for creating a new Donor in the DonorManagement database."""
    try:
        donor_db.connect()
        donor_db.execute_sql('PRAGMA foreign_keys = ON;')

        new_donor = D.create(
            donor_name=donor_name,
            donor_city=donor_city)
        new_donor.save()
        logger.info('new donor has been saved')

        logger.info('display new donor')
        adonor = D.get(donor_name=donor_name)

        logger.info(f'a new donor was just created: {adonor.donor_name}')

    except Exception as e:
        logger.info(e)

    finally:
        donor_db.close()


def list_all_donors():
    """Function to list all donors in the database."""
    try:
        donor_db.connect()
        donor_db.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Listing all Donor records: ')

        for donor in D:
            logger.info(
                f"{donor.donor_name} lives in {donor.donor_city}")

    except Exception as e:
        logger.info(e)

    finally:
        donor_db.close()


def update_donor_city(donor_name, donor_city):
    """Function for updating a Donor in the DonorManagement database."""
    try:
        donor_db.connect()
        donor_db.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Create an instance and display the donor...')
        adonor = D.get(D.donor_name == donor_name)

        logger.info(f'Found {adonor.donor_name} from {adonor.donor_city} in the database')

        adonor.donor_city = donor_city
        adonor.save()

        logger.info('Reading and print all Person records for confirmation...')

    except Exception as e:
        logger.info(e)

    finally:
        donor_db.close()


def delete_donor_record(donor_name):
    """Function for deleting a Donor from the DonorManagement database."""
    try:
        donor_db.connect()
        donor_db.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Create an instance and display the donor...')
        adonor = D.get(D.donor_name == donor_name)

        logger.info(f'Donor, {adonor.donor_name} from {adonor.donor_city}, will be removed.')

        logger.info('donor being deleted...')

        adonor.delete_instance()
        logger.info('Donor being deleted and displaying remaining donors')

        for donor in D:
            logger.info(
                f"{donor.donor_name} from {donor.donor_city}")

    except Exception as e:
        logger.info(e)

    finally:
        donor_db.close()


def add_donor_donation(donor_name, donation_amount):
    """Function for adding in a donation."""
    try:
        donor_db.connect()
        donor_db.execute_sql('PRAGMA foreign_keys = ON;')

        donation_date = date.today()

        new_donation = Donation.create(
            donation_amount=donation_amount,
            donation_date=donation_date,
            donor_name=donor_name)
        new_donation.save()

        for donate in Donation:
            logger.info(f'{donate.donor_name} - {donate.donation_amount}: given on {donate.donation_date}')
            logger.info(f'')

    except Exception as e:
        logger.info(e)

    finally:
        donor_db.close()


##################################################
# Working with the classes using the menu system #
##################################################
db = DonorDB(get_sample_data())


def quit():
    """Function for exiting the mailroom program."""
    return sys.exit("Logging out of Donation Management System")


def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    action = input(dedent('''
      Choose an action:

      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Add new donor to database
      5 - Add new donation to database
      6 - Update donor city
      7 - List all donors
      8 - Delete donor from database
      9 - Quit

      > '''))
    return action.strip()


def send_thank_you():
    """
    Record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            # print(db.list_donors())
            print(list_all_donors())
        elif name == "menu":
            return
        else:
            break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            # extra check here -- unlikely that someone will type "NaN", but
            # it IS possible, and it is a valid floating point number:
            # http://en.wikipedia.org/wiki/NaN
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        # in this case, the ValueError could be raised by the float() call, or by the NaN-check
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    # If this is a new user, ensure that the database has the necessary
    # data structure.
    # donor = db.find_donor(name)
    donor = D.get(D.donor_name)
    if donor is None:
        # donor = db.add_donor(name)
        donor = create_donor_record(name)

    # Record the donation
    donor.add_donation(amount)
    print(db.gen_letter(donor))


def print_donor_report():
    print(db.generate_donor_report())

# Get input from user to perform database operations
def get_donor_name():
    """Function for getting the donor name to work with in the database."""
    donor = input("Enter donor name or 'menu' for main menu: ")
    if donor.lower() == 'menu':
        return
    else:
        return donor


def update_donor_city_input(donor):
    """Function for updating a donor with a new city."""
    city = input("Enter donor city or 'menu' for main menu: ")
    if city.lower() == 'menu':
        return
    else:
        return update_donor_city(city, donor)


def add_donation_input(donor):
    """Function for adding a new donation to a donor."""
    donation = input("Enter donor donation amount or 'menu' for main menu: ")
    if donation.lower() == 'menu':
        return
    else:
        return add_donor_donation(donation, donor)



def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": db.save_letters_to_disk,
                      "4": create_donor_record,
                      "5": add_donation_input,
                      "6": update_donor_city_input,
                      "7": list_all_donors,
                      "8": delete_donor_record,
                      "9": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    main()
