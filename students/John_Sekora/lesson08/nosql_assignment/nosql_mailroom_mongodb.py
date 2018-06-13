"""
    Object Oriented Mail Room with Mongodb Database
"""


import utilities
import nosql_mailroom_login
from nosql_mailroom_learn_data import get_donor_list_mongodb

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


class DonorMongodb(object):
    """
    Locally stores the donor name and donation
    """

    def __init__(self, name, donation):
        self.name = name
        self.donation = donation
        self.total = 0.00


class DonorListMongodb(object):
    """
    Stores the list of donors in a dictionary and connects with a Mongodo database.
    Generates reports and sends thank you letters
    """

    def __init__(self):
        self.donor_list = {}

    def populate(self):
        """
        Initially populates database
        """
        with nosql_mailroom_login.login_mongodb_cloud() as client:
            log.info('Initializing a database called dev')
            log.info('It currently does not exist, so mongodb will create it')
            db = client['dev']

            log.info('We will create a collection called donor_list_mongodb')
            donor_list_mongodb = db['donor_list_mongodb']
            get_donor_list_mongodb()

            log.info('Populating data for donor_list_mongodb')
            donor_list_mongodb.insert_many(donor_list_mongodb)

            log.info('Populating data for donor_list_mongodb')
            self.donor_list = db.donor_list_mongodb.find()

    def add_donor(self, donor):
        """
        Adds donor and donation
        """
        if donor.name in self.donor_list.keys():
            print("Donor already exists:  {}".format(donor))
            self.donor_list[donor.name].append(donor.donation)
            print("Donation Added to existing Donor")

            try:

                with nosql_mailroom_login.login_mongodb_cloud() as client:
                    log.info('Initializing an existing database called dev')
                    db = client['dev']
                    donor_list_mongodb = db['donor_list_mongodb']
                    log.info('And in that database use a collection called donor_list_mongodb')
                    log.info('For an existing donor, add a new donation')
                    db.donor_list_mongodb.insert({'person': donor.name, 'donations': donor.donation})

                    log.info('Just saved a donation of {} from {} to the database'.format(donor.donation, donor.name))

            except Exception as e:
                log.info(e)

        else:
            self.donor_list[donor.name] = donor.donation

            try:

                with nosql_mailroom_login.login_mongodb_cloud() as client:
                    log.info('Initializing an existing database called dev')
                    db = client['dev']
                    donor_list_mongodb = db['donor_list_mongodb']
                    log.info('And in that database use a collection called donor_list_mongodb')
                    log.info('For an existing donor, add a new donation')
                    db.donor_list_mongodb.insert({'person': donor.name, 'donations': donor.donation})

                    log.info('Just saved a donation of {} from {} to the database'.format(donor.donation, donor.name))

            except Exception as e:
                log.info(e)

    def thank_you(self):
        """
        Sends a Thank You: Asks for a full name, Lists the donors, Asks for donation amount,
        Converts the donation to an integer, Adds donation amount to associated donor in list
        """
        while True:
            input_key = input("Please enter a Full Name or type 'list' to see a list of donors: ")
            if input_key == 'list':
                print("\nHere is a list of the current donors:\n")
                try:
                    with nosql_mailroom_login.login_mongodb_cloud() as client:
                        log.info('Initializing an existing database called dev')
                        db = client['dev']
                        donor_list_mongodb = db['donor_list_mongodb']

                        cursor = donor_list_mongodb.find()
                        for don in cursor:
                            print(
                                f"Cost: Donor Name: {don['person']}    Donations: {don['donations']}")

                except Exception as e:
                    log.info(e)

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
        """
        Prints a report with the Donor Name, Donations, and Total Donations.
        """
        try:
            with nosql_mailroom_login.login_mongodb_cloud() as client:
                log.info('Initializing an existing database called dev')
                db = client['dev']
                donor_list_mongodb = db['donor_list_mongodb']

                cursor = donor_list_mongodb.find()
                for don in cursor:
                    print(
                        f"Donor Name: {don['person']}, Donations: {don['donations']}, Total: {sum(don['donations'])}")

        except Exception as e:
            log.info(e)

    def letters(self):
        """
        Sends Letters
        """
        for key, val in self.donor_list.items():
            file = open('{}.txt'.format(key), 'w')
            with open('{}.txt'.format(key), 'w') as f:
                f.write("Dear {},\n\nThank You for donating a total of ${}. We look forward to hearing from you again."
                        "\n\nThe Donation Center ;^)".format(key, sum(val)))
            file.close()
        print("\n*** Text files have been created ***\n")


def menu():
    """
    Creates the user selection menu
    """
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

    dl = DonorListMongodb()
    dl.populate()

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
