#!/usr/bin/env python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 04 - Activity
     SUB TITLE: Mailroom - Metaprogramming
       CREATOR: PydPiper
  DATE CREATED: 4/28/18
 LAST MODIFIED: 5/5/18
   DESCRIPTION: Convert the 210 mailroom programming's database into JSON save/load format via metaprogramming
********************************************************************************************************************"""

""" IMPORTS """
import json_save_meta as js


class Data(js.JsonSaveable):
    # data_dict = {}
    # you have to declare a class attribute before initializing js.Dict()
    data_dict = js.Dict().default
    data = js.Dict()

    def __init__(self, name=""):
        # current name
        self.name = name
        # add to dictionary
        if name != "":
            try:
                self.data_dict[name]
            except KeyError:
                self.data_dict.update({name: [0, 0]})

    def donations(self, val=0):
        # print("data donations")
        # return current donation amount for name
        c_don = self.data_dict[self.name][0]
        c_gift = self.data_dict[self.name][1]
        if val == 0: add_gift = 0
        else: add_gift = 1
        self.data_dict.update({self.name: [val + c_don, c_gift + add_gift]})
        return self.data_dict[self.name][0]

    def gifts(self, val=None):
        if val is not None:
            c_don = self.data_dict[self.name][0]
            self.data_dict.update({self.name: [c_don, val]})
        # return current donation amount for name
        return self.data_dict[self.name][1]

    @staticmethod
    def allnames():
        return [i for i in iter(Data.data_dict)]

    @staticmethod
    def alldonations():
        return [Data.data_dict[i][0] for i in iter(Data.data_dict)]

    @staticmethod
    def allgifts():
        return [Data.data_dict[i][1] for i in iter(Data.data_dict)]

    @staticmethod
    def avgDpG():
        return [Data.data_dict[i][0]/Data.data_dict[i][1] for i in iter(Data.data_dict)]


class Donor:
    def __init__(self, name=None):
        self.name = name
        # check against data
        Data(name)

    @property
    def donations(self):
        print(self.name)
        return Data(self.name).donations()

    @donations.setter
    def donations(self, val):
        # print("in setter")
        Data(self.name).donations(val)

    @property
    def gifts(self):
        return Data(self.name).gifts()

    @gifts.setter
    def gifts(self, val):
        # overwrite current gift quantity
        Data(self.name).gifts(val)

# initialize list variables
names = ['Tony Stark', 'Captain America', 'Daisy Johnson',
     'Melinda May', 'Phil Coulson']
money = [906.04, 4500.00, 14.97, 555.02, 9999.99]
gifts = [2, 2, 3, 2, 1]
dict_data = {names[i]: [money[i], gifts[i]] for i in range(len(names))}


data_base = Data()

# convert previous data into class data
for i in range(len(names)):
    Donor(names[i]).donations = money[i]
    Donor(names[i]).gifts = gifts[i]



# ======== Send a Thank You ========
email_thx_prompt = \
"""
[OUT]: Menu: Create Thank You Note:
    1) View Donor Names
    2) Create Thank You Note
    3) Main Menu

[IN]: """
def email_thx():
    while True:
        options = input(email_thx_prompt)
        if options == "1":
            print("[OUT]: ", Data().allnames())
        if options == "2":
            email_name = input("\n[IN]: Enter donor name: ")
            if not email_name in Data.data_dict:
                print("\n[OUT]: Donor name is not on record. Adding new Donor name")
                email_money = input("[IN]: Enter new donor's donation amount = ")
                Donor(email_name).donations = float(email_money)
            print("[OUT]: Thank you {}, for donating ${}. - PydPiper".format( \
            email_name, Donor(email_name).donations))
        if options == "3": break

# ======== Create a Report ========
def report():
    print("{:<20}|{:>15}|{:>10}|{:>15}".format( \
    "Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("_"*60)
    length = len(Data().allnames())
    for i in range(length):
        print("{:<20} ${:>14} {:>10} ${:>14}".format( \
        Data().allnames()[i], Data().alldonations()[i], Data().allgifts()[i], Data().avgDpG()[i]))



# ======== Write All Emails to Files ========
def all_emails():
    length = len(Data().allnames())
    for i in range(length):
        file_name = Data().allnames()[i].replace(" ","_") + ".txt"
        with open(file_name, "w") as f:
            content = "Thank you {}, for donating ${}. - PydPiper".format( \
                Data().allnames()[i], Data().alldonations()[i])
            f.write(content)
            f.close()


# ======== Exiting ========
def exiting():
    return "exiting"

# ======== Main ========
main_prompt = \
"""
[OUT]: Menu: Main
    1) Create Thank You Note
    2) Create a Report
    3) Write out all emails
    4) Quit

[IN]: """

main_dict = {"1": email_thx, "2": report,"3": all_emails, "4": exiting}



if __name__ == "__main__":
    print("\n[OUT]: Mailroom")
    while True:
        options = input(main_prompt)
        try:
            # returns a function name from dict, then () calls it
            if main_dict[options]() == "exiting":
                with open("json_out", "w") as f:
                    data_base.to_json(f)
                break
        except KeyError:
            print("Invalid Menu Key Entered. Try again")
            continue


            

