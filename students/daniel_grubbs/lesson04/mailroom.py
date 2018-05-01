#!/usr/bin/env python3
"""
Using the Object Oriented Programming implementation done by Rick Riehl but changed it up with items from my
mailroom.py program.

The goal is to use a JSON-save system started in the Metaprogramming Lesson (week 04)
to make your model classes saveable and loadable as JSON.

Refernced article from Real Python:
https://realpython.com/python-json/
https://www.json.org/
"""
import os
import sys
from textwrap import dedent
import json

# Importing json_save for working with the data in JSON format
import json_save.json_save_dec as js

# Play around with where to place this directory path. Might need to go under the class DonorDB???
file_obj = os.path.abspath("data/donor_records.json")


@js.json_save
class Donor(object):
    """
    class to hold the information about a single donor
    """

    # Class attributes
    # It becomes apparent when looking at the constructor and the format we will be working with.
    # Need to work with the data in JSON format - here we will use:
    # string --> Donor name
    donor_name = js.String()
    # list --> Donations made by donor
    donations = js.List()

    # Let's define the data file.
    # Set initial value to None.
    # If the value is actually not None then work with it to save any changes/additions
    _donor_records = None

    # Constructor - take in the name of the donor and donations
    def __init__(self, name, donations=None):
        """
        Create a new Donor object

        :param name: the full name of the donor

        :param donations=None: iterable of past donations, name: name of the donor passed in
        """
        # Follow the example in example_dec.py
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    def transaction(func):
        """
        Method for saving items that have been changed. Apply to other methods as needed.
        This method is a decorator so it will take in another method as an argument and not self.

        :return: returns the inner function
        """

        # print("mutate (outer) method called")

        # Note from class - when using an inner function use the
        # *args and **kwargs. May not use the **kwargs but
        # add it into the inner functions anyways.
        def inner(self, *args, **kwargs):
            # print("inner method called")
            print(self._donor_records)  # is there anything in the db
            trans = func(self, *args, **kwargs)
            if self._donor_records is not None:
                self._donor_records.save()
            return trans

        return inner

    @transaction
    def donor_donation(self, donation_amt):
        """This method is for adding a donation."""
        # Should add in the donation as a float so
        # if donation_amt is not already a float then
        # simply make sure it is  using float()
        donation_amt = float(donation_amt)
        self.donations.append(donation_amt)

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
        donations made using len() on the donations list.
        """
        return self.total_donations / len(self.donations)

    def letter_template(self):
        """Template for writing a letter to a donor, thanking them for their donation."""
        return """Dear {},\nThank you for your very kind donation of {:.2f}.\n\nIt will be put to very good use.\n\n \t\tSincerely,\n\t\t\t-The Team""".format(
            self.name, self.last_donation)


@js.json_save
class DonorDB(object):
    """
    Encapsulation of the entire database of donors and data associated with them.
    """

    # Class attributes
    # Will be using a dictionary here to work with it
    donor_records = js.Dict()

    def __init__(self, donors=None, donor_data=None):
        """
        Initialize a new donor database

        :param donors=None: iterable of Donor objects; data_file=None: access the file named _file.json
        """
        # Database
        # Does it exist?
        if donor_data is None:
            self.donor_data = "data/donor_records.json"
        else:
            self.donor_data = donor_data

        # Donors
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    @property
    def donors(self):
        """Method to get the donor values."""
        return self.donor_data.values()

    def list_donors(self):
        """
        creates a list of the donors as a string, so they can be printed
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """Method for looking up a donor."""
        return self.donor_data.get(Donor.normalize_name(name))

    def add_donor(self, name):
        """Add a new donor to donor_records."""
        donor = Donor(name)
        self.donor_data[donor.norm_name] = donor
        return donor

    def gen_letter(self, donor):
        """Generate a thank you letter for the donor."""
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

    def donor_save_records(self, file):
        """Save donor and information related to donor."""
        # Open donor_records.json in write mode an save to the file.
        with open(self.donor_data, 'w') as file_obj:
            self.to_json(file_obj)

    @classmethod
    def load_donor_records_from_file(cls, file):
        """Load the donor and information from file. Uses a file that is in json format already."""
        # Open donor_records.json using context manager
        with open(file) as f_obj:
            donors = json.load(f_obj)
        # lookp through the donors and append to the donor_list
        donor_list = []
        # loop through the donors pulled from the file
        for donor in donors:
            donor_list.append(donor)

        # return the list of donors from the file
        return donor_list

    @classmethod
    def load_donor_records_js(cls, file):
        """Method for working with the json_save library."""
        # Open donor_records.json using context manager
        with open(file) as f_obj:
            donors = js.from_json(file_obj)
        donors.donor_data = file

    def create_donor_report(self):
        """Create a report of the donors and donation amounts."""
        donations = []

        print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Number of Gifts",
                                                        "Average Gifts"))
        print("-" * 80)

        for donor, gift in self.donor_records.values():
            total_given = sum(gift)
            number_gifts = len(gift)
            average_gift = total_given / number_gifts
            donations.append((donor, total_given, number_gifts, average_gift))

        for amount in donations:
            print("{:26s} | {:14.2f} | {:15d} | {:13.2f}".format(*amount))
        print()

    def save_letters_to_disk(self):
        """Method to save letters to disk for each of the donors in the database."""
        for donor in self.donor_data.values():
            print("Writing a letter to:", donor.name)
            letter = self.gen_letter(donor)
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)

        print('Completed creating letters to send out to donors.')


##################################################
# Working with the classes using the menu system #
##################################################
data_dir = os.path.abspath("data/donor_records.json")
donor_db = DonorDB()
records = DonorDB.load_donor_records_from_file(data_dir)
initial_data_set = {
    'Jimmy Nguyen': [100, 1350, 55],
    'Steve Smith': [213, 550, 435],
    'Julia Norton': [1500, 1500, 1500],
    'Ed Johnson': [150],
    'Elizabeth McBath': [10000, 1200]
}



def quit():
    """Function for exiting the mailroom program."""
    return sys.exit(0)


def thank_you():
    """Function for Thank you. Prompts for a donors name."""
    while True:
        full_name = input(
            "Please enter a donor's name or type 'list' for list of donors ('menu' to return to menu): ").strip()

        if full_name == 'list':
            print('Below is the current donor list:')
            print(donor_db.list_donors())
        elif full_name == 'menu':
            return
        else:
            break

    # Enter a donation amount
    while True:
        donation = int(input("Please enter a donation amount. 'menu' to return to original menu: "))
        if donation == 'menu':
            return
        try:
            donate = float(donation)
        except ValueError:
            print('Please enter a valid amount.')
        else:
            break

    # Enter a new donor
    donor = DonorDB.find_donor(full_name)
    if donor is None:
        donor = donor_db.add_donor(full_name)

    # Add in donation for the donor
    donor.donor_donation(donate)

    # Print the donor letter
    print(donor.letter_template())

    print(Donor.letter_template(donor_obj, donor))


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
    menu_selection = {
        1: thank_you,
        2: donor_db.create_donor_report,
        3: donor_db.save_letters_to_disk,
        4: quit
    }
    main()
