#!/usr/bin/env python3
"""
The goal is to use a JSON-save system started in the Metaprogramming Lesson (week 04)
to make your model classes saveable and loadable as JSON.

Refernced article from Real Python:
https://realpython.com/python-json/
https://www.json.org/
"""
# Imports for mailroom
import os
import sys
from pathlib import Path

# Importing json_save for working with the data in JSON format
import json_save.json_save_dec as js


# Play around with where to place this directory path. Might need to go under the Donor class???
# file_obj = os.path.abspath("data/donor_records.json")


@js.json_save
class DonorDonations(object):
    """
    Class to hold the records of a donor and their donations.
    """

    # Class attributes
    # It becomes apparent when looking at the constructor and the format we will be working with.
    # Need to work with the data in JSON format - here we will use:
    # string --> Donor name
    donor_name = js.String()
    # list --> Donations made by donor
    donations = js.List()
    # May not be needed but adding in case need it
    initial_state = False

    # Constructor - take in the name of the donor and donations
    def __init__(self, donor_name, donations=None):
        """Constructor for instantiating a donor."""
        # Follow the example in example_dec.py
        # self.donor_name = donor_name
        # self.donations = []
        self.donor_name = donor_name
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @property
    def first_name(self):
        forename = self.donor_name.split()
        return forename[0]

    @property
    def last_name(self):
        surname = self.donor_name.split()
        return surname[1]

    @property
    def last_donation(self):
        """Grab the most recent donation from the list of donations."""
        try:
            # We want the last donation so we want to use the negative index
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        """Total up all the donations that were made by a donor."""
        return sum(self.donations)

    @property
    def average_donation(self):
        """Take the total_donations that were calculated and divide by the amount of
        donations made using len() on the donations list."""
        return self.total_donations / len(self.donations)

    def letter_template(self):
        """Template for writing a letter to a donor, thanking them for their donation."""
        return """Dear {}{},\n
        Thank you for your very kind donation of ${:.2f}.\n\n
        It will be put to very good use.\n\n \t\tSincerely,\n\t\t\t
        -The Team""".format(
            self.first_name,
            self.last_name,
            self.last_donation
        )


@js.json_save
class Donor(object):
    """
    Encapsulation of the entire database of donors and data associated with them.
    """
    # Class attributes
    # Will be using a dictionary here to work with it
    db = None
    donor_records = js.Dict()
    initial_state = False

    def __init__(self, donors=None, donor_data=None):
        """Initialize a new donor database."""
        # Database
        # Does it exist?
        if donor_data is None:
            self.donor_data = os.path.abspath("data/donor_records.json")
        else:
            self.donor_data = Path(donor_data)

        self.donor_records = {}

        # Donors
        if donors is not None:
            self.initial_state = True
            for i in donors:
                self.add_donor(i)

    @property
    def donors(self):
        """Method to get the donor values."""
        return self.donor_records.values()

    def add_donor(self, donor):
        """Add a donor."""
        if not isinstance(donor, DonorDonations):
            donor = DonorDonations(donor)
        self.donor_records[donor] = donor
        donor.db = self
        return donor

    def list_donors(self):
        """Method to create a list of the donors as a string, so they can be printed."""
        donor_list = ["Donor list:"]
        for donor in self.donors:
            donor_list.append(donor.donor_name)
        return "\n".join(donor_list)

    def donor_lookup(self, name):
        """Method for looking up a donor."""
        return self.donor_records.get(DonorDonations(name))

    def donor_save_records(self):
        """Save donor and information related to donor."""
        # Open donor_records.json in write mode an save to the file.
        with open(self.donor_data, 'w') as donor_data:
            self.to_json(donor_data)

    @classmethod
    def load_donor_records_js(cls, file):
        """Class method for working with the json_save library."""
        # Open donor_records.json using context manager
        with open(file) as f_obj:
            temp_donors = js.from_json(f_obj)
        temp_donors.donor_data = file

    def create_donor_report(self):
        """Create a report of the donors and donation amounts."""
        # Set an empty list for donations to append donations to as they are iterated over.
        donations = []

        print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Number of Gifts",
                                                        "Average Gifts"))
        print("-" * 80)
        # print(self.donor_records.values())

        for donor in self.donor_records.values():
            full_name = donor.name
            gifts = donor.donor_donation
            total_given = donor.total_donations
            number_gifts = len(gifts)
            average_gift = donor.average_donation
            donations.append((full_name, total_given, number_gifts, average_gift))

        for amount in donations:
            print("{:26s} | {:14.2f} | {:15d} | {:13.2f}".format(*amount))
        print()

        return donations

    def gen_letter(self, donor):
        """Generate a thank you letter for the donor."""
        """Template for writing a letter to a donor, thanking them for their donation."""
        return """Dear {0:s},\nThank you for your very kind donation of ${1:.2f}.\n\nIt will be put to very good use.\n\n \t\tSincerely,\n\t\t\t-The Team""".format(
            donor, donor.last_donation)

    def send_letter_file(self):
        """Write a thank you letter and save to file."""
        for k, v in donor_data.values():
            letter = gen_letter(donor)
            file_name = donor.name.replace(" ", "_") + ".txt"
            with open(file_name, 'w') as f:
                f.write(letter)

        print('Completed creating letters to send out to donors.')


##################################################
# Working with the classes using the menu system #
##################################################
# data_dir = os.path.abspath("data/donor_records.json")
# records = Donor.load_donor_records_js(data_dir)
# print(records)

def quit():
    """Function for exiting the mailroom program."""
    return sys.exit("Logging out of Donation Management System")


def thank_you():
    """Function for Thank you. Prompts for a donors name."""
    while True:
        full_name = input(
            "Please enter a donor's name or type 'list' for list of donors ('menu' to return to menu): ").strip()

        if full_name == 'list':
            print('Below is the current donor list:')
            d = donor_in.list_donors
            # print(donor_in.list_donors)
            print(d)
        elif full_name == 'menu':
            return
        else:
            break

    # Enter a donation amount
    while True:
        donation = float(input("Please enter a donation amount. 'menu' to return to original menu: "))
        if donation == 'menu':
            return
        try:
            donate = float(donation)
        except ValueError:
            print('Please enter a valid amount.')
        else:
            break

    # Enter a new donor
    donor = donor_in.find_donor(full_name)
    if donor is None:
        donor = donor_in.add_donor(full_name)

    # Add in donation for the donor
    donor.donor_donation(donate)

    # Print the donor letter
    # print(donor.letter_template())
    print(DonorDonations.letter_template(donor))


def print_header():
    """Prints the menu items to choose from and returns the selection."""
    print('------------------------------------------')
    print('       Donation Management System')
    print('                v0.1.7\n')
    print('       1: Send A Thank You')
    print('       2: Create A Report')
    print('       3: Send Letters To Everyone')
    print('       4: Quit\n')
    print('------------------------------------------\n')

    try:
        selection = int(input('Please select a menu item: '))
    except ValueError:
        print('Your selection is invalid. Please make a selection from the menu.')
        selection = int(input('Please select a menu item: '))

    return selection


def main():
    """Main mneu of the program."""
    while True:
        try:
            menu_selection[print_header()]()
        except KeyError:
            print('Your selection did not match any item in the menu. Please make another selection.')
            continue


if __name__ == '__main__':
    donor_in = Donor()
    initial_data = [
    ["Jimmy Nguyen", [653772.32, 12.17]],
    ["Steve Smith", [877.33, 55.67]],
    ["Julia Norton", [663.23, 43.87, 1.32]],
    ["Ed Johnson", [1663.23, 4300.87, 10432.15]],
    ["Elizabeth McBath", [1663.23, 4300.87, 10432.25]]
]

    menu_selection = {
        1: thank_you,
        2: donor_in.create_donor_report,
        3: donor_in.send_letter_file,
        4: quit
    }
    main()
