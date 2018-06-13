#!/usr/bin/env python3

import logging
import uuid
from pymongo import MongoClient
from mysetting import settings

logging.basicConfig(level=logging.CRITICAL)

client = MongoClient(port=27017)
db = client.sampleDB

class LoadToDB:
    def __init__(self):
        pass

    def db_con(self):
        logging.info("Establishing connection to database")
        self.database = MongoClient("mongodb://{username}:{password}@{host}/{database}?{options}".format(**settings()))

    def db_discon(self):
        logging.info("Database closed")
        self.database.close()

    def check_unique(self, iname):
        try:
            Donor.get(Donor.name == iname)
            logging.info(f"{iname} is on record")
            return False
        except Exception as e:
            logging.info(f"{iname} is not on record")
            logging.info(e)
            return True

    def add(self, iname, idonation=0.0):
        # gift count to account for entry that is name only, or zero donation specified
        if idonation == 0:
            gift_count = 0
        else:
            gift_count = 1
        self.db_con()
        if self.check_unique(iname):
            logging.info(f"Adding new donor {iname}, with a donation of ${idonation}")
            with self.database.transaction():
                new_person = Donor.create(name=iname)
                new_donation = Donation.create(gift_num=gift_count,
                                               value=idonation,
                                               donated_by=iname,
                                               gift_id=uuid.uuid4())
                # new_person.save()
                # new_donation.save()
                logging.info('Database add successful')
                print(f"{iname} has been added to the Database")
        else:
            logging.info(f"Donor {iname} already on record, adding ${idonation} to existing funds.")
            old_d = Donation.get(Donation.donated_by == iname).value
            old_g = Donation.get(Donation.donated_by == iname).gift_num
            # only try to add to Donation primary key if donation amount dont not equal zero
            if gift_count > 0:
                with self.database.transaction():
                    new_donation = Donation.create(gift_id=uuid.uuid4(), gift_num=(old_g + 1),
                                                   value=(old_d + idonation),
                                                   donated_by=iname)
                    # new_donation.save()
                    logging.info('Database add successful')
                    print(f"{iname} with a donation of ${idonation:.2f} has been added to the Database")
        self.db_discon()

    def remove(self, iname):
        self.db_con()
        if self.check_unique(iname):
            print("Name is not on record")
        else:
            query = Donor.get(Donor.name == iname)
            query.delete_instance()
            query = Donation.get(Donation.donated_by == iname)
            query.delete_instance()
            print(f"{iname} removed from Database")
        self.db_discon()

    def remove_donation(self, iname, igift):
        self.db_con()

        try:
            query = Donation.get(Donation.donated_by == iname, Donation.gift_num == igift)
        except Exception as e:
            logging.info(f"{iname} with {igift} is not on record of Donation DB")
            logging.info(e)
        else:
            if int(igift) >= 1:
                query.delete_instance()
                print(f"{iname} gift number {igift} removed from Database")
        self.db_discon()


class PullFromDB(LoadToDB):
    @property
    def all_names(self):
        """
        Calls on DB and returns a list of names
        :return: list of strings
        """
        self.db_con()
        names = []
        for donor in Donor:
            names.append(donor.name)
        self.db_discon()
        return names

    def all_donations(self, iname):
        """
        Calls on DB and returns a list of donation for a person
        :return: dictionary of floats
        """
        self.db_con()
        rtn_doncations = {}
        index = 0

        if self.check_unique(iname=iname):
            print(f"{iname} is not on record.")
        else:
            # databaseObject.select returns back as a peewee object, it can be iterated over as a Model but not
            # directly (ie for donations in query.donation.donations will throw an error when trying to . extend
            # to donation from the query) This step must be done within the loop as shown below.
            # .get is different where it returns the DB value directly (not a peewee object)
            query = Donor.select(Donor, Donation).join(Donation, JOIN.INNER).where(Donor.name == iname)
            for donor in query:
                rtn_doncations.update({index: donor.donation.value})
                index += 1

        self.db_discon()
        return rtn_doncations

    def total_donations(self, iname):
        """
        Calls on DB and returns all donations summed up for a given donor
        :param iname: str, donor name
        :return: float, sum of all donations
        """
        self.db_con()
        rtn_funds = 0

        if self.check_unique(iname=iname):
            print(f"{iname} is not on record.")
            self.db_discon()
            return None
        else:
            query = Donor.select(Donor, Donation).join(Donation, JOIN.INNER).where(Donor.name == iname)
            for donor in query:
                rtn_funds += donor.donation.value

        self.db_discon()
        return rtn_funds

    def total_gifts(self, iname):
        self.db_con()

        if self.check_unique(iname=iname):
            print(f"{iname} is not on record.")
            return None
        else:
            rtn_tot_gifts = int(Donation.get(Donation.donated_by == iname).gift_num)

        self.db_discon()
        return rtn_tot_gifts

    def avg_DpG(self, iname):
        try:
            avg = self.total_donations(iname) / self.total_gifts(iname)
        except ZeroDivisionError:
            avg = 0
        return avg


def Menu_AddRem():
    Menu_Data_prompt = \
        """
        Menu 0-1: Entry/Retrieval
            1) View Donor Names
            2) Add Name
            3) Add Donation to Name
            4) Delete Name
            5) Delete Donation from Name
            b) Main Menu
    
        [IN]: """

    while True:
        option = input(Menu_Data_prompt)
        if option == "1":
            print(pullfromDB.all_names)
        if option == "2":
            user_name = input("Enter a NEW donor name: ")
            if loadtoDB.check_unique(iname=user_name):
                loadtoDB.add(iname=user_name)
            else:
                print(f"{user_name} is already on record.")
        if option == "3":
            user_name = input("Enter the name of a EXISTING Donor: ")
            if not loadtoDB.check_unique(iname=user_name):
                user_donation = float(input("Enter a Donation Amount $: "))
                if user_donation <= 0:
                    print("Donation Amount must be greater than or equal to $0")
                else:
                    loadtoDB.add(iname=user_name, idonation=user_donation)
            else:
                print(f"{user_name} is not on record. A donation must be assigned to Donor prior to donating.")
                while True:
                    user_yesno = input("Enter donation as Anonymous? (yes/no)")
                    if user_yesno == "yes":
                        user_name = "Anonymous"
                        user_donation = float(input("Enter a Donation Amount $: "))
                        if user_donation <= 0:
                            print("Donation Amount must be greater than or equal to $0")
                        else:
                            loadtoDB.add(iname=user_name, idonation=user_donation)
                        break
                    elif user_yesno == "no":
                        break
                    else:
                        print("Invalid input, type ""yes"" or ""no""")
        if option == "4":
            user_name = input("Enter the name of a EXISTING Donor: ")
            if not loadtoDB.check_unique(iname=user_name):
                loadtoDB.remove(iname=user_name)
            else:
                print(f"{user_name} is not on record.")
        if option == "5":
            user_name = input("Enter the name of a EXISTING Donor: ")
            if not loadtoDB.check_unique(iname=user_name):
                d_list = pullfromDB.all_donations(iname=user_name)
                # Donation has at least 1 entry to delete
                if len(d_list) > 1:
                    print(d_list)
                    user_gift = input("Enter which gift to delete (number from 1 to {}: ".format(len(d_list)-1))
                    loadtoDB.remove_donation(iname=user_name, igift=user_gift)
                else:
                    print(f"{user_name} has no donations to delete")
            else:
                print(f"{user_name} is not on record.")
        if option == "b":
            break
        if option not in "12345b":
            print("Invalid entry, select again from the Menu Options")

def Menu_Report():
    print("Menu 0-2: Report 0-2")
    print("{:<20}|{:>15}|{:>10}|{:>15}".format("Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("_"*60)

    n_list = pullfromDB.all_names
    for names in n_list:
        print("{:<20} ${:>14} {:>10} ${:>14}".format(names,
                                                     pullfromDB.total_donations(iname=names),
                                                     pullfromDB.total_gifts(iname=names),
                                                     pullfromDB.avg_DpG(iname=names)))


def Menu_Email_Single():
    Menu_Email_Single_prompt = \
        """
        Menu 0-3: Single Email Note:
            1) View Donor Names
            2) Create Thank You Note
            b) Main Menu
    
        [IN]: """

    while True:
        option = input(Menu_Email_Single_prompt)
        if option == "1":
            print(pullfromDB.all_names)
        if option == "2":
            user_name = input("Enter donor name: ")
            tot_d = pullfromDB.total_donations(iname=user_name)
            if tot_d is not None:
                print("Thank you {}, for donating ${}. - PydPiper".format(user_name, tot_d))
        if option == "b":
            break
        if option not in "12b":
            print("Invalid entry, select again from the Menu Options")


def Menu_Email_All():
    print("Menu 0-4: Email All")
    n_list = pullfromDB.all_names
    for names in n_list:
        tot_d = pullfromDB.total_donations(iname=names)
        file_name = names.replace(" ", "_") + ".txt"
        with open(file_name, "w") as f:
            content = "Thank you {}, for donating ${}. - PydPiper".format(names, tot_d)
            f.write(content)
            f.close()


def Menu_Exiting():
    return "exiting"


if __name__ == "__main__":
    loadtoDB = LoadToDB(dbname)
    pullfromDB = PullFromDB(dbname)

    Main_prompt = \
        """
        Menu 0: Main
            1) Data Entry/Retrieve
            2) Create a Report
            3) Create Thank You Note
            4) Write out all emails
            q) Quit
    
        [IN]: """
    main_dict = {"1": Menu_AddRem, "2": Menu_Report, "3": Menu_Email_Single, "4": Menu_Email_All, "q": Menu_Exiting}

    while True:
        options = input(Main_prompt)
        try:
            # returns a function name from dict, then () calls it
            if main_dict[options]() == "exiting":
                break
        except KeyError:
            print("Invalid Menu Key Entered. Try again")
            continue


            

