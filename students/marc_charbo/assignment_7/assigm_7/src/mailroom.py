from src import donors_data as DonorData
from peewee import *
from src.data_model import Person, Donation
from pprint import pprint

donor_helpers = DonorData.DonorData()

def send_letter():
    """write thank you note to all users in donor list"""
    donor_helpers.save_letters()

def quit():
    print('Existing program\n')
    return 'quit'

def create_report():
    """ prints donnation report on sreen.
        for each user their name, sum of donnations, number of times they donnated
        and avg donnation amount is displayed.
    """
    print (donor_helpers.print_report())

    print('-- End Report --\n')

def send_email(selection,amount):
    """ sends thank you email to donor with their name and donation amount"""
    print('-- Sending Email --\n')
    print ('Thank you {} for you generous ${:.2f} donation'.format(selection,amount))
    print('-- Email Sent --\n')

def send_thank_you():
    """ donnor dict handling function"""
    selection = input('Enter a donors username or list to see all donors: ')

    database = SqliteDatabase('mailroom.db')

    if selection == 'list':
        print('Here is the list of donors in the database')

        try:
            database.connect()
            database.execute_sql('PRAGMA foreign_keys = ON;')

            for person in Person:
                pprint(
                    f'This username {person.username} with first name {person.person_first_name} with first name {person.person_last_name}')

        except Exception as e:
            print(e)

        finally:
            database.close()

    else:
        try:
            database.connect()
            database.execute_sql('PRAGMA foreign_keys = ON;')
            donor = Person.get(Person.username == selection)

            if donor is not None:
                print ('{} was found in the database'.format(donor))

            else:
                first_name = input('Enter a donors first name: ')
                last_name = input('Enter a donors last names: ')
                new_person = Person.create(
                    username= selection,
                    person_first_name= first_name,
                    person_last_name= last_name)
                new_person.save()
                print('{} was added to the database'.format(selection))

            try:
                amount = input('Please enter a donation amount: ')
                amount = float(amount)
                new_donation = Donation.create(
                    donation_date = '2108-06-02',
                    donation_amount = amount,
                    person_donated = selection)
                new_donation.save()
                send_email(selection,amount)

            except ValueError as e:
                print('error with task running program\n {}'.format(e))
                print('Returning to main menu\n')
                return

        except Exception as e:
            print(e)

        finally:
            database.close()



def prompt_user():
    """ function which displays main menu and prompts user to enter selection"""
    print('Please select one of three options: ')
    print('1- Send a Thank You')
    print('2- Create a Report')
    print('3- Send letters to everyone')
    print('4- Quit')
    selection = input('Enter your selection: ')

    return int(selection)

dispatch_dict = {1: send_thank_you, 2: create_report, 3: send_letter, 4: quit}

def run():
    """ function which runs program"""
    print ("Welcome to Donation Manager")
    while True:
        try:
            if dispatch_dict[prompt_user()]() == 'quit':
                break
        except KeyError as e:
            print('{} select not available please chose between menu options\n'.format(e))
            continue
        except ValueError as e:
            print('{} select not available please chose between menu options\n'.format(e))

def main():
    try:
        run()
    except Exception as e:
        print ('error with task running program\n {}'.format(e))

if __name__ == "__main__":
    main()