import sys


donor_data = {"sai emani": [20.23, 30.456, 50.786],
                   "sirisha marthy": [67.89, 45.89],
                   "ani emani": [12.789, 5.456],
                   "charles dickens": [15.89, 89.20, 345.67],
                   "mark twain": [678.986]
                   }


class Donor(object):
    def __init__(self, name, donations):
        if not name:
            raise ValueError("Donor name can not be empty")
        self.name = name
        if not donations:
            self.donations = []
        else:
            self.donations = donations

    @property
    def first_name(self):
        name_split = self.name.split()
        if len(name_split) >= 1:
            return name_split[0]

    @property
    def last_name(self):
        name_split = self.name.split()
        if len(name_split) == 1:
            return ''
        else:
            return ''.join(name_split[1:])
    @property
    def donor_donations(self):
        """
        Returns list of donor donations
        :return: list of donor donations
        """
        return self.donations
    @property
    def donor_donations_sum(self):
        """
        Returns sum of all donor donations
        :return: donor latest donation
        """
        return sum(self.donations)
    @property
    def latest_donation(self):
        """
        Returns donor latest donation
        :return: donor latest donation
        """
        if self.donations:
            return self.donations[-1]

    def add_donation(self, amount):
        """
        Adds donation to donor donations
        :return:
        """
        if float(amount) <= 0:
            raise ValueError("donation amount can not be negative")
        self.donations.append(float(amount))

    def generate_letter(self):
        """ Generate letter for donor """
        return "Dear {},\n \nThank you for your generous donation {}.\n \n\n\t\tSincerely, \n\t\tLocal Charity". \
            format(self.name, self.latest_donation)

class Donors(object):
    def __init__(self, donors_list=None):
        # list of donors objects
        if not donors_list:
            self.donors_list = []
        else:
            self.donors_list = donors_list
    @property
    def list_of_donors(self):
        return [donor.name for donor in self.donors_list]

    @property
    def count(self):
        return len(self.donors_list)

    def add_donor(self, donor):
        self.donors_list.append(donor)

    def get_donor(self, name):
        if name == "":
            return None

        for donor in self.donors_list:
            if donor == name:
                return donor
        new_donor = Donor(name, [])
        self.add_donor(new_donor)
        return new_donor

    def send_letters(self):
        """ Send letters to every one, the letters will be stored as text files on disk """
        for donor in self.donors_list:
            file_name = donor.name + ".txt"
            letter = donor.generate_letter()
            with open(file_name, "w") as f:
                f.write(letter)

    def create_a_report(self):
        """ Prints donor information for all donors
        """
        print("Donor Name                | Total Given | Num Gifts | Average Gift")
        for donor in self.donors_list:
            if donor.donations:
                print(f"{donor.name:26} $ {sum(donor.donations):>10.2f}   {len(donor.donations):9} "
                    f"${sum(donor.donations)/len(donor.donations):>12.2f}")
            else:
                print("coming to else")

    def load_donors_list(self):
        temp_list = []
        donations = []
        for donor in donor_data:
            donor_obj = Donor(donor, donations)
            donor_obj.donations = donor_data[donor]
            temp_list.append(donor_obj)
        self.donors_list =  temp_list
        return self.count

    def save_donors_list(self):
        for donor in self.donors_list:
            if donor.name not in donor_data:
                donor_data[donor.name] = donor.donations
        return self.count

    def total_contribution(self):
        return sum([sum(d.donations) for d in self.donors_list])

    def challenge(self, mul, min_donation=None, max_donation=None):
        if min_donation and max_donation:
            def func(x): return  max_donation > x > min_donation

        elif min_donation:
            def func(x): return x > min_donation

        elif max_donation:
            def func(x): return x < max_donation
        else:
            def func(x): return True

        return Donors([Donor(donor.name, list(map(lambda x: x ** mul, filter(func, donor.donations))))
                       for donor in self.donors_list])


def send_a_thankyou(donors_obj):
    """ Sends thank you message for the donors
    """
    while True:
        name = str(
            input("Please enter donor name (enter \"list\" to show list of donor names, enter \"q\" to quit)"))
        if name == "q":
            return
        elif name == "list":
            print("List of donor names")
            print(("{}\n" * donors_obj.count).format(*donors_obj.list_of_donors))
            continue
        else:
            donor = donors_obj.get_donor(name)
            if not donor:
                print("Name can not be empty")
                continue
            else:
                break
    while True:
        try:
            amount = input("Please enter donation amount")
            if float(amount) <= 0:
                print("amount donated must be a +ve number")
            else:
                break
        except ValueError:
            print("Enter positive number")
    donor.add_donation(amount)
    #for donor in donors_obj.donors_list:
     #   print("Donor name {} and donation {}".format(donor.name, donor.donations))
    print(donor.generate_letter())

def menu(menu_data):

    """ Select one of the four items in the menu
        And returns the number """

    print("\nPlease choose one of the following options:")

    for index, menu_item in enumerate(menu_data):  # Prints the menu user text
        print(f"{index + 1}) {menu_item[0]}")

    choice = int(input("> ")) - 1

    if choice in range(len(menu_data)):  # Ensure that option chosen is within menu range, this
        return menu_data[choice][1], menu_data[choice][2]  # handles choosing 0, which would return menu_data[-1][1]

    return None


def make_projections(donors_obj):

    min =0
    max =0
    mul = 1

    projection = donors_obj.challenge(mul, min, max)
    def set_value():
        while True:
            try:
                value = float(input("Set value >"))
                if value <= 0:
                    print("Must be a positive number")
                else:
                    break
            except ValueError:
                print("Please enter a numerical value")
        return value

    while True:
        projections_menu = [
            ("enter min amount for multiplier to take effect. [Currently ${}]".format(mul), set_value, 'min'),
            ("enter max amount for multiplier to take effect. [Currently ${}]".format(mul), set_value, 'max'),
            ("enter a multiplier value. [Currently {}]".format(mul), set_value, 'mul'),
            ("print report past distributions", donors_obj.create_a_report, None),
            ("Print projected distributions", projection.create_a_report, None),
            ("print total contributed comparison", "compare_total", None),
            ("quit menu", 'quit', None)
        ]

        fn , param = menu(projections_menu)
        if param == 'min':
            min = fn()
        elif param == 'max':
            max = fn()
        elif param == mul:
            mul = fn()

        if param:
            projection = donors_obj.challenge(mul, min, max)
        elif fn == 'compare_total':
            print(f"Original total contribution: {donors_obj.total_contribution():.2f}")
            print(f"Projeected total contribution: {projection.total_contribution():.2f}")
        elif fn  == 'quit':
            return
        else:
            fn()

if __name__ == "__main__":
    donors_obj = Donors()
    menu_fns = [
        ('Send thank you', send_a_thankyou, donors_obj),
        ('create a report', donors_obj.create_a_report, None),
        ('send letters to every one', donors_obj.send_letters, None),
        ('load donors list', donors_obj.load_donors_list, None),
        ('save donors list', donors_obj.save_donors_list, None),
        ('quit', sys.exit, None)
    ]

    #choice_dict = {1: send_a_thankyou, 2: donors_obj.create_a_report, 3: donors_obj.send_letters,
     #              4: donors_obj.load_donors_list, 5: donors_obj.save_donor_list, 6: sys.exit}
    while True:
        try:
            fn , param = menu(menu_fns)
            if param:
                fn(param)
            else:
                fn()
        except TypeError:
            continue
        except ValueError:
            continue





