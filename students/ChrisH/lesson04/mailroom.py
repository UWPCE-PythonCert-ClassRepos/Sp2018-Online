#!/usr/bin/env python3
# -----------------------------------------------------------
# mailroom.py
#  Script to automate writing thank you emails to donors.
# -----------------------------------------------------------

import time
from sys import exit
import pickle


class Donors(object):

    DATA_FILE = 'donors.pkl'

    def __init__(self, donorlist=None):
        if donorlist:
            self.donorlist = donorlist
        else:
            self.donorlist = []

    def add_donor(self, donor):
        self.donorlist.append(donor)

    def print_report(self):
        """
        Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
        :return: None
        """
        # Find longest name in donor list, or use name_min value
        if self.donorlist:
            name_max = max(*[len(donor.name) for donor in self.donorlist], 25)
        else:
            name_max = 25

        rpt_title = "Donor Name" + ' ' * (name_max - 9) + "| Total Given | Num Gifts | Average Gift"
        print(rpt_title)
        print("-" * len(rpt_title))
        for donor in self.donorlist:
            print(f"{donor.name:{name_max}}  ", end='')
            ddons = donor.donations
            print(f"$ {sum(ddons):>10.2f}   {len(ddons):>9}  ${sum(ddons)/len(ddons):>12.2f}")

    def send_letters_all(self):
        """
            Runs through donor data structure, generates a thank you letter for each and saves it to
            the current working directory with in a date+donorname.txt file
            :return: None
            """
        for donor in self.donorlist:
            print(f'Generating letter for {donor.name}')
            now = time.localtime()
            f_name = f"{now.tm_year}{now.tm_mon:02}{now.tm_mday:02}_"
            f_name += donor.name.replace(" ", "_") + ".txt"
            with open(f_name, 'w') as file_out:
                file_out.write(donor.generate_letter())
        return None

    @property
    def list_donors(self):
        return [donor.name for donor in self.donorlist]

    @property
    def count(self):
        return len(self.donorlist)

    def get_donor(self, dname):
        if dname == "":
            return None

        for donor in self.donorlist:
            if donor.name == dname:
                return donor

        newdonor = Donor(dname)
        self.add_donor(newdonor)
        return newdonor

    def load_donorlist(self):
        with open(self.DATA_FILE, 'rb') as file_in:
            self.donorlist = pickle.load(file_in)
        return self.count

    def save_donorlist(self):
        with open(self.DATA_FILE, 'wb') as file_out:
            pickle.dump(self.donorlist, file_out)
        return self.count

    def total_contribution(self):
        return sum([sum(d.donations) for d in self.donorlist])


    def challenge(self, mul, min_don=None, max_don=None):
        """
        Multiplies donations, returns a Donors object.
        Note that this function destroys the original order of the donations, as multiplied donation values get
        grouped together, and non-multiplied donations get moved to the end of the list.
        :param mul: a multiplier to be applied to each donation value of each donor
        :param min_don: multiplier only applies to values greater than this amount, if None - does not apply
        :param max_don: multiplier only applies to values less than or equal to this amount, if None - does not apply
        :return: a new Donors object, with multiplied donation values
        """

        # define the filter functions, based on if min or max values for donation multipliers were added
        # unfortunately, PEP8 abhors assigning lambdas to variables, so here are some glorious Defs.
        #  fi = donations that should be multiplied
        #  not_fi = donations that should not be multiplied
        if min_don and max_don:
            def fi(x): return max_don >= x > min_don

            def not_fi(x): return x <= min_don or x > max_don

        elif min_don:
            def fi(x): return x > min_don

            def not_fi(x): return x <= min_don

        elif max_don:
            def fi(x): return x <= max_don

            def not_fi(x): return x > max_don
        else:
            def fi(x): return True

            def not_fi(x): return False

        # iterate the donorlist, apply filters to the list of donations for each donor, multiply the donations on only
        #   one of the filters, add these two donation lists together, slap it together with the donors' name to create
        #   a donor object. List comprehension makes a list of the new Donors, which is then used as an input to create
        #   a new Donors() class object.
        return Donors(
            [Donor(
                donor.name,
                list(map(lambda y: y * mul, filter(fi, donor.donations))) + list(filter(not_fi, donor.donations))
            ) for donor in self.donorlist]
        )


class Donor(object):

    def __init__(self, name, donations=None):
        if not name:
            raise ValueError("Donor name cannot be empty.")
        self.name = name
        if not donations:
            self.donations = []
        else:
            self.donations = donations

    @property
    def first(self):
        name_sp = self.name.split()
        if len(name_sp) == 1:
            return ''
        else:
            return name_sp[0]

    @property
    def last(self):
        name_sp = self.name.split()
        if len(name_sp) == 1:
            return self.name
        else:
            return ' '.join(name_sp[1:])

    def add_donation(self, amount):
        if float(amount) <= 0:
            raise ValueError('Donation amount must be a positive number.')
        else:
            self.donations.append(amount)

    @property
    def last_donation(self):
        if not self.donations:
            return None
        else:
            return self.donations[-1]

    def generate_letter(self):
        """
        Generates a Thank You letter to send to a donor. Uses the last value in their donations list to
        mention their last donation amount.
        :param donor: a donor dictionary entry
        :return: string containing the text of the Thank You letter.
        """
        format_string = """
Dear {first_name} {last_name},

   Thank you for your donation of ${last_donation:.2f}.

            Warmest Regards,
                Local Charity
"""
        return format_string.format(
            last_donation=float(self.last_donation),
            first_name=self.first,
            last_name=self.last
        )


def send_thank_you_menu(dlist):
    """
    Prompts for donor name, if not present, adds user to data. Prompts for donation
    and adds it to donor's data. Prints a 'Thank You' email populated with the donor's data.
    :return: None
    """

    while True:
        name = input("Enter a Full Name ('list' to show list of donors, 'q' to quit): ")
        if name == 'q':
            return
        elif name == 'list':
            print(("{}\n" * dlist.count).format(*dlist.list_donors))
            continue
        else:
            donor = dlist.get_donor(name)
            if not donor:
                print("Name cannot be empty.")
                continue
            else:
                break

    while True:
        try:
            amount = float(input(f"Enter a donation amount for {donor.name} : "))
            if amount <= 0:
                print('Amount donated must be a positive number.')
            else:
                break
        except ValueError:
            print('Please enter a numerical value.')

    donor.add_donation(amount)
    print(donor.generate_letter())


def make_projections(dlist):

    dmin = 0
    dmax = 0
    dmul = 1
    projection = dlist.challenge(dmul, dmin, dmax)

    def set_val():
        while True:
            try:
                value = float(input("set value > "))
                if value <= 0:
                    print('Must be a positive number.')
                else:
                    break
            except ValueError:
                print('Please enter a numerical value.')
        return value

    while True:
        menu_projections = [
            ("enter min amount that multiplier will affect. [Currently ${}]".format(dmin), set_val, 'dmin'),
            ("enter max amount that multiplier will affect. [Currently ${}]".format(dmax), set_val, 'dmax'),
            ("enter a multiplier value. [Currently {}]".format(dmul), set_val, 'dmul'),
            ("print report past contributions", dlist.print_report, None),
            ("print report projected contributions", projection.print_report, None),
            ("print total contribution comparison", 'compare_total', None),
            ("quit to main menu", 'quit', None),
        ]

        fn, param = menu(menu_projections)
        if param == 'dmin':
            dmin = fn()
        elif param == 'dmax':
            dmax = fn()
        elif param == 'dmul':
            dmul = fn()

        # if a parameter is not None, then values have been updated, so update the projection
        if param:
            projection = dlist.challenge(dmul, dmin, dmax)
        elif fn == 'compare_total':
            print(f"Original total contribution: {dlist.total_contribution():.2f}")
            print(f"Projected total contribution: {projection.total_contribution():.2f}")
        elif fn == 'quit':
            return
        else:
            fn()


def menu(menu_data):
    """
    Prints the main user menu & retrieves user selection.
    :param: a menu list, consisting of iterable with three values:
        [0]: text to be presented to user
        [1]: function that should be called for the menu item
        [2]: parameter that should be used in the function call, None if no parameter call needed
    :return: two values:
        1) the function corresponding to the user's selection, or None on a bad selection
        raises ValueError if choice is non-numeric
        2) a parameter that should be used with the fn call, None if no parameter needed
    """
    print("\nPlease choose one of the following options:")

    for index, menu_item in enumerate(menu_data):   # Prints the menu user text
        print(f"{index + 1}) {menu_item[0]}")

    choice = int(input("> ")) - 1

    if choice in range(len(menu_data)):                     # Ensure that option chosen is within menu range, this
        return menu_data[choice][1], menu_data[choice][2]   # handles choosing 0, which would return menu_data[-1][1]

    return None


if __name__ == "__main__":

    dl = Donors()

    menu_functions = [
        ('Send a Thank You', send_thank_you_menu, dl),
        ('Print a report', dl.print_report, None),
        ('Send letters to everyone', dl.send_letters_all, None),
        ('Make donation projections', make_projections, dl),
        ('Load donor list', dl.load_donorlist, None),
        ('Save donor list', dl.save_donorlist, None),
        ('Quit', exit, None),
    ]
    while True:
        try:
            fn, param = menu(menu_functions)
            if param:
                fn(param)
            else:
                fn()
        except TypeError:
            continue
        except ValueError:
            continue
