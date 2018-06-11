"""
    Object Oriented Mail Room with Neo4j Database
"""


import utilities
import nosql_mailroom_login

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


class DonorNeo4j(object):
    """
    Locally stores the donor name and donation
    """

    def __init__(self, name, donation):
        self.name = name
        self.donation = donation
        self.total = 0.00


class DonorListNeo4j(object):
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
        log.info('Clear the entire database')
        log.info("Running clear_all")
        driver = nosql_mailroom_login.login_neo4j_cloud()
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

        with driver.session() as session:

            # Adding Donors with Donations
            log.info('Adding initial Donor and Donation nodes')
            for donor, donations in [('John Smith', [400]),
                                     ('Bill Wilmer', [8000, 10000, 3000]),
                                     ('George Guy', [50]),
                                     ('Nathan Star', [250.50, 100]),
                                     ]:
                cyph = "CREATE (n:Donor_List {donor:'%s', donations: '%.2f'})" % (donor, donations)
                session.run(cyph)

    def add_donor(self, donor):
        """
        Adds donor and donation
        """
        if donor.name in self.donor_list.keys():
            print("Donor already exists:  {}".format(donor))
            self.donor_list[donor.name].append(donor.donation)
            print("Donation Added to existing Donor")

            log.info("Adding donation for donor to neo4j database")
            driver = nosql_mailroom_login.login_neo4j_cloud()
            with driver.session() as session:
                cyph = "CREATE (n:Donation {donations:'%.2f'})" % (donor.donation)
                session.run(cyph)

                log.info('Creating associations between Donor and new Donation')
                cyph = """
                          MATCH (p1:Donation {donations: str(donor.donation)})
                          CREATE (p1)-[association:Associate]->(p2:Donor {donor:'%s', donations:'%.2f'})
                          RETURN p1
                        """ % (donor.name)
                session.run(cyph)

        else:
            print("Adding new donor:  {}".format(donor))
            self.donor_list[donor.name] = donor.donation
            print("Donation Added to existing Donor")

            log.info("Adding new donor and donation to neo4j database")
            driver = nosql_mailroom_login.login_neo4j_cloud()
            with driver.session() as session:
                cyph = "CREATE (n:Donor {donor:'%s'})" % (donor.name)
                session.run(cyph)
                cyph = "CREATE (n:Donation {donations:'%.2f'})" % (donor.donation)
                session.run(cyph)

                log.info('Creating associations between New Donor and New Donation')
                cyph = """
                          MATCH (p1:Donation {donations: str(donor.donation)})
                          CREATE (p1)-[association:Associate]->(p2:Donor {donor:'%s', donations:'%.2f'})
                          RETURN p1
                        """ % (donor.name)
                session.run(cyph)

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

    dl = DonorListNeo4j()
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
