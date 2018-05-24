#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom with jason load and save
# Dev: Scott Luse
# Date: 04/28/2018
# -------------------------------------------------#

'''
mailroom_meta status 5/01
1. test data is loaded at startup
2. json data is saved to donors.txt using menu item 4
3. Code is in place to load the json from donors.txt
4. Code needs to be add to deserialize data
4a. My logic may be incorrect, unable to get past this point
'''

import sys
import json_save.json_save_meta as js


def load_test_data():
    #test data should not be used in json meta programming assignment
    return [donor_record("Peter Parker", [288.09, 9.01, 61288.09]),
            donor_record("Iron Man", [1238.09, 8199.01, 1468.07]),
            donor_record("Captain Marvel", [43188.09, 1288.09]),
            donor_record("Black Widow", [10.00, 10.00]),
            ]

def create_from_saved(myfile):
    print("\nParse this data and create database: " + str(myfile))

class donor_record():

    def __init__(self, name, donations=None):
        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, amount):
        amount = float(amount)
        self.donations.append(amount)


class donor_database(js.JsonSaveable):

    dl = js.List()

    def __init__(self, donors=None):
        self.donor_data = {d: d for d in donors}

    def save_to_file(self, filename):
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            temp = [name, gifts]
            self.dl.append(temp)

        print(self.dl)

        '''
        with open(filename, 'w') as outfile:
            json.dump(self.dl, outfile)
            print("\njson dump complete!")
        '''

        with open(filename, 'w') as outfile:
            self.to_json(outfile)
        print("\nto_json complete!")


    @classmethod
    def load_from_file(cls, filename):
         with open(filename, 'r') as infile:
             obj = js.from_json(infile)
         print("\nfrom_json complete!")
         return obj

    @property
    def donors(self):
        return self.donor_data.values()

    def donor_list(self):
        listing = []
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        return self.donor_data.get(name)

    def add_donor(self, name):
        print('Donor added: ' + name)
        donor = donor_record(name)
        self.donor_data[donor] = donor
        return donor

    def print_screen_report(self):
        print('')
        print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
        print('-' * 55)
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            num_gifts = len(gifts)
            total_gifts = "{:.2f}".format(donor.total_donations)
            avg_gift = "{:.2f}".format(donor.average_donation)
            print('{:20}{:>15}{:>10}{:>10}'.format(name, total_gifts, num_gifts, avg_gift))


    def create_individual_letters(self):
        try:
            for donor in self.donor_data.values():
                name = donor.name
                total_gifts = donor.total_donations
                file_name = name.replace(" ", "_") + ".txt"
                my_file = open(file_name, "w")
                my_file.write(gen_letter_body(name, total_gifts))
                my_file.close()
        except IOError:
            return ("\n" + "File error!")
        return ("*** Files saved! ***")


#loading test data
#database = donor_database(load_test_data())


#loadind saved data from json file
mydata = donor_database.load_from_file("donors.txt")
print("from_json data: " + str(mydata))
print("Add code to deserialize the data...")


def gen_letter_body(name, amount):

    report_text = (f'''Dear {name},

    Thank you for your charitable gift of ${amount}.

                It will be put to very good use.


                                Sincerely,
                                        --The Cool Team''')
    return (report_text)

def thank_you_printing(name, amount):
    line_divider = "*" * 50
    print(f'''
    {line_divider}
    {name}
    Address

    Dear {name},
    Thank you for your charitable gift of ${amount}.
    {line_divider}
    ''')

def send_thanks():
    while (True):
        name = input("Please enter FULL NAME, enter 'LIST' for names, or 'MAIN' for menu: ")
        if name.lower() == "list":
            print(database.donor_list() + "\n")
        elif name.lower() == "main":
            return
        else:
            process_thank_you(name)

def process_thank_you(name):
    '''
    Prompt the user for a donation amount following the prompt for donor name.
    This function is being refactored during meta programming assignment
    '''
    try:
        gift_amount = int(input("Please enter donation $$ AMOUNT for " + name + ":"))
        list = database.donor_list()
        if name in list:
            print('\nSorry, updating an old donor feature is not refactored. Try creating a new donor!\n\n ')
        else:
            donor = database.add_donor(name)
            donor.add_donation(gift_amount)
            thank_you_printing(name, gift_amount)
    except ValueError as e:
        print("\n Error: " + str(e) + "\nPlease enter a number amount:\n ")
        process_thank_you(name)

def get_user_choice():
    '''Generates a main menu selection (1-4) for user actions.'''
    print("""
    MailRoom Meta Programming Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Save Database (json)
    5) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 5]: ")
    return (user_choice.strip())

def process_menu(menu_item):
    if menu_item == '1':
        send_thanks()
    elif menu_item == '2':
        database.print_screen_report()
    elif menu_item == '3':
        print(database.create_individual_letters())
    elif menu_item == '4':
        database.save_to_file("donors.txt")

def quit():
    sys.exit(0)

def main():
    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "5":
            print("Goodbye!")
            quit()
        else:
            process_menu(get_user_action)

if __name__ == '__main__':

    main()
