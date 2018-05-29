#!/usr/bin/env python3

"""Mailroom - Lesson 8 Adv Python - using a neo4j cloud db."""

import os
import datetime
import tkinter as tk
from tkinter import filedialog
# import login_database
import configparser
from pathlib import Path
from neo4j.v1 import GraphDatabase, basic_auth

# GETTING USER AND PASSWORD DATA FROM CONFIG FILE
config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
config.read(config_file)
graphenedb_user = config["configuration"]["user"]
graphenedb_pass = config["configuration"]["pw"]
graphenedb_url = "bolt://hobby-bjkmfeabkpihgbkeddhdlgbl.dbs.graphenedb.com:24786"

driver = GraphDatabase.driver(graphenedb_url,
                              auth=basic_auth(graphenedb_user, graphenedb_pass))

####################
# SINGLE DONOR CLASS
####################
class SingleDonor():
    """Provide a class for a single donor."""

    def __init__(self, _name, _donations):
        """Instantiate a SingleDonor class object."""
        self._name = _name
        if isinstance(_donations, list):
            self._donations = _donations
        elif isinstance(_donations, tuple):
            self._donations = list(_donations)
        else:
            self._donations = [_donations]

    @property
    def name(self):
        """Provide a getter method for the name property."""
        return self._name

    @property
    def donations(self):
        """Provide a getter method for the donations property."""
        return self._donations

    def sort_by_total(self):
        """Provide a sort_key for sorting by total donations."""
        return sum(self._donations)

    def sort_by_name(self):
        """Provide a sort_key for sorting by name."""
        return self._name

    def __str__(self):
        """Return self._name."""
        return self._name

    def __repr__(self):
        """Return SingleDonor("Name", [donations])."""
        if len(self._donations) == 1:
            return 'SingleDonor("{}", {})'.format(self._name,
                                                  self._donations[0]
                                                  )
        else:
            return 'SingleDonor("{}", {})'.format(self._name,
                                                  self._donations
                                                  )

    def __eq__(self, other):
        """Return True if names and donations are the same."""
        return (self._name, self._donations) == (other.name, other.donations)

    def __lt__(self, other):
        """Provide __lt__ method used in sorting somehow, I guess."""
        return ((self._name, self._donations) <
                (other.name, other.donations)
                )

    def add_donation(self, amount):
        """Add a donation directly to db and a relation to donor."""
        with driver.session() as session:
            node_name = "".join(self.name.split()) + "Donation"
            new_gift_id = len(self.donations)

            #  Create the node for donation - string concatenation here
            #  because node labels can't be parametrized
            cyph = ("CREATE (c:" + node_name + "{donation: " + str(amount)
                    + ", id: " + str(new_gift_id) + "})")

            session.run(cyph)

            #  Establish a relationship between donor and donoation node
            cyph = ("MATCH (a:Person), (b:" + node_name + ")" + "\n"
                    + "WHERE a.person_name = " + "'" + self.name + "'" + "\n"
                    + "CREATE  (a)-[h:HAS_DONATIONS]->(b) " + "\n"
                    + "RETURN h" + "\n")
            session.run(cyph)

    def get_last_donation(self):
        """Return the last donation."""
        return self._donations[-1]


##############
# DONORS CLASS
##############
class Donors():
    """Provide a class to handle a collection of donors."""

    def __init__(self, donors):
        """Instantiate a Donors class object with a list of SingleDonors."""
        self._donors = donors

    def __iter__(self):
        """Make the Donors class object iterable."""
        return iter(self._donors)

    def __contains__(self, donor_str):
        """Provide a method to check if donor (expects a str) is in donors."""
        return donor_str in [donor.name for donor in self._donors]

    def get_donor(self, name):
        """Given a name (str), return the donor object, or raise ValueError."""
        for donor in self._donors:
            if donor.name == name:
                return donor
        else:
            raise ValueError("No such donor exists")

    def append(self, donor, amount):
        """Create in the graph db - donor:str, amount:float; and link them."""
        with driver.session() as session:
            # Create person
            cyph = """CREATE (p:Person {person_name: '%s'})""" % (donor)
            session.run(cyph)

            # Create donation node - string concatenation here
            #  because node labels can't be parametrized
            gift_label = "".join(donor.split()) + "Donation"
            cyph = ("CREATE (c:" + gift_label + "{donation: " + str(amount)
                    + ", id: " + str(0) + "})")
            session.run(cyph)

            #  Establish a relationship between them
            cyph = ("MATCH (a:Person), (b:" + gift_label + ")" + "\n"
                    + "WHERE a.person_name = " + "'" + donor + "'" + "\n"
                    + "CREATE  (a)-[h:HAS_DONATIONS]->(b) " + "\n"
                    + "RETURN h" + "\n")
            session.run(cyph)



    def print_donor_names(self):
        """Print existing donor names on screen in alphabetical order."""
        donors_L = [donor.name for donor in sorted(self._donors,
                                                   key=SingleDonor.sort_by_name
                                                   )
                    ]
        num = len(donors_L)
        donors_S = (("\n" + ", ".join(["{}"] * num)).format(*donors_L))
        print(donors_S)

    def create_report(self):
        """Create and print a report."""
        report = ""
        title_line_form = "\n{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}\n"
        title_line_text = ('Donor Name', '|', 'Total Given', '|',
                           'Num Gifts', '|', 'Average Gift'
                           )
        report += title_line_form.format(*title_line_text)
        report += str('- ' * 38)
        form_line = "\n{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
        donors_list = sorted(self._donors,
                             key=SingleDonor.sort_by_total,
                             reverse=True)
        for donor in donors_list:
            report += (form_line.format(donor.name,
                                        '$',
                                        sum(donor.donations),
                                        ' ',
                                        len(donor.donations),
                                        '$',
                                        round((sum(donor.donations) /
                                               len(donor.donations)),
                                              2)
                                        )
                       )
        report += "\n"
        print(report)


##################
# START MENU CLASS
#################
class StartMenu(object):
    """Provide a class for user ineraction via prompts and menus."""

    def __init__(self):
        """Launch main menu."""
        self.menu_selection(self.main_menu_prompt(), self.main_menu_dispatch())

    # lOADING DONOR DATABASE
    def donors(self):
        """Load donors from db and return it as a Donors class object."""
        try:
            # Get donor info from db and convert it into Donors class
            with driver.session() as session:
                # Step 1: Get people names from db.
                try:
                    people_names = []
                    cyph = """MATCH (p:Person)
                              RETURN p.person_name as person_name
                              """
                    result = session.run(cyph)
                    for donor in result:
                        people_names.append(donor['person_name'])
                    # print(people_names)
                except Exception as e:
                    print("Failed to query for people in the db: ", e)

                # Step 2: Get donations for each person from S.1
                try:
                    people_donations = []
                    for name in people_names:
                        cyph = """
                          MATCH (p:Person {person_name: '%s'})
                                -[:HAS_DONATIONS]->(personDonations)
                          RETURN personDonations
                          ORDER by personDonations.id
                          """ % (name)
                        result = session.run(cyph)
                        a_list_gifts = []
                        for rec in result:
                            for donation in rec.values():
                                a_list_gifts.append(float(donation['donation']))
                        people_donations.append(a_list_gifts)
                    # print(people_donations)
                except Exception as e:
                    print("Failed to query for donations in the db: ", e)

                # Step 3: Convert results from S.1 and S.2 into a dict
                dict_donors_gifts = dict(zip(people_names, people_donations))

            # Convert the dict with donors as keys and donations as values into
            # a Donors class object
            return Donors([SingleDonor(key, value) for key, value in
                           dict_donors_gifts.items()
                           ]
                          )

        except Exception as e:
            print("Having a problems with loading the db because", e)

    # MANAGING MENUS
    # Template for dispatch dicts
    def menu_selection(self, prompt, dispatch_dict):
        """Provide a template for using dispatch dicts to go through menus."""
        while True:
            response = input(prompt)
            try:
                if dispatch_dict[response]() == "exit menu":
                    break
            except KeyError:
                print("\nInvalid choice. Try again")

    # Quit option for menus
    def quit(self):
        """Provide an exit option for menus."""
        return "exit menu"

    # Main menu
    def main_menu_dispatch(self):
        """Return a dispatch dict for the main menu."""
        return {"1": self.send_thank_you_sub_menu,
                "2": self.create_report,
                "3": self.send_all_sub_menu,
                "4": self.remove_donor,
                "0": self.quit,
                }

    def main_menu_prompt(self):
        """Return a prompt str for the main menu."""
        return ("\nMain Menu\n"
                "\n1 - Send a Thank You\n"
                "2 - Create a Report\n"
                "3 - Send letters to everyone\n"
                "4 - Delete a donor from the db\n"
                "0 - Quit\n"
                ">> "
                )

    # Send-a-Thank-You Sub-Menu
    def send_thank_you_sub_menu(self):
        """Initiate the send-thank-you sub-menu."""
        self.menu_selection(self.send_thank_you_prompt(),
                            self.send_thank_you_dispatch()
                            )

    def send_thank_you_dispatch(self):
        """Return a dispatch dict for the send-thank-you sub-menu."""
        return {"1": self.print_donor_names,
                "2": self.new_donor_interaction,
                "3": self.old_donor_interaction,
                "0": self.quit,
                }

    def send_thank_you_prompt(self):
        """Return a prompt str for the send-thank-you sub-menu."""
        return ("\nSend-Thank-You Sub-Menu\n"
                "\n1 - See the list of donors\n"
                "2 - Add a new donor and a donation amount\n"
                "3 - Choose an existing donor\n"
                "0 - Return to Main Menu\n"
                ">> "
                )

    def print_donor_names(self):
        """Provide a wrapper method to call donors.print_donor_names."""
        # When I call it directly from dispatch dict, it does not work
        # 'cos, I assume, its value is evaluated once in the dispatch dict
        # when the program first starts running
        # and does not change later during the program execution
        self.donors().print_donor_names()

    def create_report(self):
        """Provide a wrapper method to call donors.create_report method."""
        # When I call it directly from dispatch dict, it does not work
        # 'cos, I assume, its value is evaluated once in the dispatch dict
        # when the program first starts running
        # and does not change later during the program execution
        self.donors().create_report()

    def get_email(self, name, amount):
        """Return a str containing a thank-you email."""
        email_text = ("""\nDear {},\n
                      \nI would like to thank you for your donation of ${}.\n
                      \nWe appreciate your support.\n
                      \nSincerely,\n
                      \nThe Organization\n
                      """).format(name, amount)
        return email_text

    def input_donation(self, name):
        """Obtain the donation amount from the user."""
        prompt_amount = "Enter the donation amount or 0 to abort > "
        while True:
            try:
                donation_amount = float(input(prompt_amount))
            except ValueError:
                print("Input must be a number")
            else:
                if donation_amount == 0.0:
                    return False
                elif donation_amount < 0:
                    print("Input must not be negative")
                else:
                    try:
                        donor = self.donors().get_donor(name)
                    except ValueError:  # name is a new donor - create him
                        self.donors().append(name, donation_amount)
                    else:
                        donor.add_donation(donation_amount)
                    return True

    def new_donor_interaction(self):
        """Call old_donor_interaction() but for the new donor functionality."""
        # This method is called from a distpatch dict and its only purpose is
        # to enable me to pass an argument, i.e. old=False,
        # to the old_donor_interaction() method below.
        # The intention is to make the user choose first if he wants
        # to create a new donor or use an old one. If the user doesn't
        # remember old donors, he can choose to see a list of old donors.
        # An alternative suggested was to get rid of this functionality
        # and just create a new donor every time the user enters a name
        # which is not on the list of the old donors.
        # I didn't like this option because it'd be similar to creating a new
        # email account every time the user misspells his name when he logs in,
        # if I may use this analogy.
        self.old_donor_interaction(old=False)

    def old_donor_interaction(self, old=True):
        """Ask for donor name, donation amount, print a thank-you email."""
        prompt_name = "Type the donor's full name or 0 to abort > "
        if old:
            name = ""
            while name not in self.donors():
                name = input(prompt_name)
                if name == "0":
                    return
        else:
            while True:
                name = input(prompt_name)
                if name == "0":
                    return False
                elif name == "":
                    print("Name must not be empty!")
                else:
                    break

        if self.input_donation(name):
            print(self.get_email(name,
                                 self.donors().get_donor(name).get_last_donation()
                                 )
                  )

    #  Send-letters-to-everyone Sub-Menu - Writing to files
    def send_all_sub_menu(self):
        """Initiate the send-all-letters sub-sub-menu."""
        self.menu_selection(self.send_all_prompt(),
                            self.send_all_dispatch())

    def send_all_dispatch(self):
        """Return a dispatch dict for the send-to-everyone sub-menu."""
        return {"1": self.write_cwd,
                "2": self.write_select_dir,
                "0": self.quit,
                }

    def send_all_prompt(self):
        """Return a prompt str for the send-to-everyone sub-menu."""
        return ("\nSend to everyone sub-menu\n"
                "\n1 - Write to current working directory\n"
                "2 - Choose a directory to write\n"
                "0 - Return to Main Menu\n"
                ">> "
                )

    def get_full_path(self, destination, name):
        """Construct a full path including date and name."""
        date = str(datetime.date.today())
        filename = "{}-{}.txt".format(date, name)
        path = os.path.join(destination, filename)
        return path

    def write_file(self, destination, text):
        """Write text to destination path."""
        with open(destination, "w") as toF:
            toF.write(text)

    def write_cwd(self):
        """Write all emails to the current working directory."""
        cwd = os.getcwd()
        for donor in self.donors():
            text = self.get_email(donor.name,
                                  donor.get_last_donation()
                                  )
            self.write_file(self.get_full_path(cwd, donor.name), text)

        print("\nAll letters saved in {}\n".format(cwd))

    def ask_user_dir(self):
        """Get a directory from the user."""
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory()

    def write_select_dir(self):
        """Write all emails to a dir selected by the user."""
        target_dir = self.ask_user_dir()
        if not target_dir:  # If the user hits cancel.
            return
        for donor in self.donors():
            text = self.get_email(donor.name, donor.get_last_donation())
            self.write_file(self.get_full_path(target_dir, donor.name), text)

        print("\nAll letters saved in {}\n".format(target_dir))


    def remove_donor(self):
        """Prompt use for donor name to delete and delete the record."""
        while True:
            response = input("Type donor you want to delete or 0 to go back > ")
            if response == "0":
                break
            else:
                query = Person.select().where(Person.person_name == response)
                if query.exists():
                    try:
                        name = Person.get(Person.person_name == response)
                        if name.delete_instance() == 1:
                            print("{} deleted successfully".format(response))
                            break
                    except Exception as e:
                        print('Problem deleting this record because', e)
                else:
                    print("No such donor. Try again or 0 to go to Main Menu")


if __name__ == "__main__":
    StartMenu()
