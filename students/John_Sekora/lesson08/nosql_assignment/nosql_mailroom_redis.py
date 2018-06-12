"""
    Object Oriented Mail Room with Redis Database
"""


import utilities
import nosql_mailroom_login

log = utilities.configure_logger('default', '../logs/redis_script.log')


class DonorRedis(object):
    """
    Locally stores the donor name and donation
    """

    def __init__(self, name, donation):
        self.name = name
        self.donation = donation
        self.total = 0.00


class DonorListRedis(object):
    """
    Stores the list of donors in a dictionary and connects with a Redis database.
    Generates reports and sends thank you letters
    """

    def __init__(self):
        self.donor_list = {}

    def populate(self):
        """
        Initially populates database
        """
        self.donor_list = [
            {
                'person': 'John Smith',
                'donations': [400],
            },
            {
                'person': 'Bill Wilmer',
                'donations': [8000, 10000, 3000],
            },
            {
                'person': 'George Guy',
                'donations': [50],
            },
            {
                'person': 'Nathan Star',
                'donations': [250.50, 100],
            }
        ]

        try:
            log.info('Connecting to Redis')
            r = nosql_mailroom_login.login_redis_cloud()

            log.info('Cache some data in Redis')
            r.set('John Smith', [400])
            r.set('Bill Wilmer', [8000, 10000, 3000])
            r.set('George Guy', [50])
            r.set('Nathan Star', [250.50, 100])

        except Exception as e:
            print(f'Redis error: {e}')

    def add_donor(self, donor):
        """
        Adds donor and donation
        """
        if donor.name in self.donor_list.keys():
            print("Donor already exists:  {}".format(donor))
            self.donor_list[donor.name].append(donor.donation)
            print("Donation Added to existing Donor")
            try:
                log.info('Connecting to Redis')
                r = nosql_mailroom_login.login_redis_cloud()

                log.info('Adding donation to existing donor in Redis')
                r.set(donor.name, donor.donation)

            except Exception as e:
                log.info(e)

        else:
            self.donor_list[donor.name] = donor.donation
            try:
                log.info('Connecting to Redis')
                r = nosql_mailroom_login.login_redis_cloud()

                log.info('Adding new donor and donation to Redis')
                r.set(donor.name, donor.donation)

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
                    log.info('Connecting to Redis')
                    r = nosql_mailroom_login.login_redis_cloud()

                    log.info('Displaying Donors and Donations')
                    redis_data = r.get()
                    print(redis_data)

                except Exception as e:
                    log.info(e)

            decision = input("Would you like to add an email address and zip code?")
            if decision.lower == "y" or "yes":
                email = input("Please enter email for {}: ".format(input_key))
                zip_code = input("Please enter zip code for {}: ".format(input_key))
                try:
                    log.info('Connecting to Redis')
                    r = nosql_mailroom_login.login_redis_cloud()
                    r.set(str(input_key), email, zip_code)
                except Exception as e:
                    log.info(e)

            elif input_key in self.donor_list.keys():
                while True:
                    try:
                        input_value = float(input("Enter a donation amount for {} : ".format(input_key)))
                        try:
                            log.info('Connecting to Redis')
                            r = nosql_mailroom_login.login_redis_cloud()
                            r.rpush(str(input_key), input_value)
                        except Exception as e:
                            log.info(e)

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
                    try:
                        log.info('Connecting to Redis')
                        r = nosql_mailroom_login.login_redis_cloud()
                        r.set(str(input_key), input_value)
                    except Exception as e:
                        log.info(e)

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
        """ Prints a report with the Donor Name, Total Given, Number of Gifts, and Average Gift. """
        print("Donor Name                | Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------------")
        for key, val in self.donor_list.items():
            print(f"{key:25} $ {float(sum(val)):>12.2f}  {len(val):>8}  $ {float(sum(val))/len(val):>11.2f}")

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

    def email_zip(self):
        """
        adds email and zip code for a donor
        """
        while True:
            donor_entered = input("Please enter a donor...")
            email = input("Please enter an email address...")
            zip_code = input("Please enter a zip code...")

            try:
                log.info('Connecting to Redis')
                r = nosql_mailroom_login.login_redis_cloud()
                if donor_entered in r.get():
                    r.set(str(donor_entered), email, zip_code)
                    break
                else:
                    continue
            except Exception as e:
                log.info(e)

    def search(self):
        """
        Searches email and zip code for donor
        """
        while True:
            donor_search = input("Please enter a donor to search email address and zip code...")

            try:
                log.info('Connecting to Redis')
                r = nosql_mailroom_login.login_redis_cloud()
                if donor_search in r.get():
                    print("Here are the results for {}: ".format(donor_search))
                    print(
                        f'Email: {r.lindex(str(donor_search), 1)}  Zip Code:{r.lindex(str(donor_search), 2)}')
                    break
                else:
                    continue
            except Exception as e:
                log.info(e)


def menu():
    """
    Creates the user selection menu
    """
    while True:
        print("\nPlease select an option:")
        print("1. Thank You  |  2. Report  |  3. Letters  |  4. Add Email/Zip Code  |  5. Search Donor  |  6. Quit")
        try:
            menu_selection = int(input())
        except ValueError as e:
            print("Exception occurs in menu_selection: {}".format(e))
            break
        else:
            return menu_selection


if __name__ == '__main__':

    dl = DonorListRedis()
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
            dl.email_zip()
        elif choice == 5:
            dl.search()
        elif choice == 6:
            print("\n***\nYou have chosen to Exit the program. Goodbye!\n***")
            quit(4)
