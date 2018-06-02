#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom menu
# Dev: Scott Luse
# Date: 06/02/2018
# Change log:
# added mongodb
# -------------------------------------------------#


import mongodb_donor as mongo
import utilities
import sys


def donor_name_input(option):
    name = input("Please enter donor NAME or 'main' for the menu: ")
    if name.lower() == "main":
        return
    else:
        process_name(option, name)

def donor_delete_record(name):
    amount = input("DELETE: Please enter gift AMOUNT or 'main' for the menu: ")
    if amount.lower() == "main":
        return
    else:
        mongo.donor_delete_entry(amount, name)

def donor_modify(name):
    amount = input("Please enter donation AMOUNT or 'main' for the menu: ")
    if amount.lower() == "main":
        return
    else:
        mongo.donor_create_update(amount, name)

def process_name(option, name):
    if option == '1':
        donor_modify(name)
    elif option == '2':
        donor_modify(name)
    elif option == '3':
        donor_delete_record(name)

def get_user_choice():
    '''
    Main menu selection
    '''
    print("""
    MailRoom noSQL Programming Menu Options
    1) Add Donor To Database
    2) Add Financial Gift ($)
    3) Delete Single Gift Record
    4) Create Screen Report
    5) Drop Collection!
    6) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 6]: ")
    return (user_choice.strip())

def quit():
    sys.exit(0)

def main():

    log = utilities.configure_logger('default', '../logs/mailroom_mongodb.log')
    log.info("Starting Main")

    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "6":
            print("Goodbye!")
            quit()
        elif get_user_action == '5':
            mongo.donor_drop_collection()
        elif get_user_action == '4':
            mongo.donor_screen_report()
        else:
            donor_name_input(get_user_action)

if __name__ == '__main__':
    main()
