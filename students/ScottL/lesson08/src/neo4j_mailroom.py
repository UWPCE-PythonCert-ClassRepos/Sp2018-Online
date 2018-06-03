#!/usr/bin/env python3

# -------------------------------------------------#
# Title: neo4j_mailroom menu
# Dev: Scott Luse
# Date: 06/02/2018
# Comments: need to add delete record; more investigation
# required to use the cyph MATCH for a specific persons
# donation records
# -------------------------------------------------#


import neo4j_donor as neo4j
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
        neo4j.donor_delete_entry(amount, name)

def donor_modify(name):
    amount = input("Please enter donation AMOUNT or 'main' for the menu: ")
    if amount.lower() == "main":
        return
    else:
        neo4j.donor_create_update(amount, name)

def process_name(option, name):
    if option == '1':
        donor_modify(name)
    elif option == '2':
        donor_modify(name)
    elif option == '3':
        print("Delete record not working...")

def get_user_choice():
    '''
    Main menu selection
    '''
    print("""
    MailRoom noSQL neo4j Menu Options
    1) Add Donor To Database
    2) Add Financial Gift ($)
    3) Delete Single Gift Record
    4) Create Screen Report
    5) Detach and Delete!
    6) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 6]: ")
    return (user_choice.strip())

def quit():
    sys.exit(0)

def main():

    log = utilities.configure_logger('default', '../logs/mailroom_neo4j.log')
    log.info("Starting Main")

    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "6":
            print("Goodbye!")
            quit()
        elif get_user_action == '5':
            neo4j.donor_detach_delete()
        elif get_user_action == '4':
            neo4j.donor_screen_report()
        else:
            donor_name_input(get_user_action)

if __name__ == '__main__':
    main()
