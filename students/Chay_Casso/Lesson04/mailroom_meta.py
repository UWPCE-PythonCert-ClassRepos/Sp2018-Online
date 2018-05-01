#!/usr/bin/env python3
#
# Mailroom Meta
# Chay Casso, 4/29/18

from collections import OrderedDict

import json_save.json_save_dec as js


@js.json_save
class Mailroom(object):

    # Initial donor table with the donation values.
    donor_table_dict = js.Dict()


    def __init__(self, donor_table_dict):
        self.donor_table_dict = donor_table_dict

    def thank_you(self, thank_you_dict, full_name, donation_value_str):
        output_string = ""
        while True:
            if full_name.lower() == "quit": return thank_you_dict, ""
            if full_name.lower() == "list":
                output_string = "Donor list:\n"
                for i in (list(thank_you_dict.keys())):
                    output_string = output_string + i + "\n"
                return thank_you_dict, output_string
            else:
                if donation_value_str.lower() == "quit": return thank_you_dict, ""
                try:
                    donation_value_flt = float(donation_value_str)
                    if donation_value_flt <= 0:
                        raise ValueError
                    if full_name in thank_you_dict:
                        thank_you_dict[full_name].append(donation_value_flt)
                    else:
                        thank_you_dict[full_name] = [donation_value_flt]
                    print()
                    output_string = ("""
Dear {}:
    Thank you for your generous donation of ${:.2f} to Save the Kids.

-------------
Save the Kids
save@kids.org
                    """.format(full_name, donation_value_flt))
                    return (thank_you_dict, output_string)
                except ValueError:
                    output_string = "Not entered. Please enter a positive number value for the donation amount."
                    return thank_you_dict, output_string

    def create_report(self, create_report_dict):
        output_string = "{:<20} | {:<10} | {:<10} | {:<10}\n".format("Donor Name", "Total Given", "Num Gifts",
                                                                     "Average Gift")
        output_string += "----------------------------------------------------------------------------\n"
        order_dict = OrderedDict(sorted(create_report_dict.items()))
        for key in order_dict:
            output_string += (
                "{:<20}   ${:>10.2f}   {:>10d}   ${:>10.2f}\n".format(key, sum(order_dict[key]), len(order_dict[key]),
                                                                      sum(order_dict[key]) / len(order_dict[key])))
        return create_report_dict, output_string

    def send_letters(self, send_letters_dict):
        for key in send_letters_dict:
            with open(key + ".txt", "w") as writefile:
                letter = """
Dear {}:
    Thank you for your recent donation of ${:.2f} to Save the Kids. We are grateful for your total donations of ${:.2f} 
    to our organization.

-------------
Save the Kids
save@kids.org
""".format(key, send_letters_dict[key][-1], sum(send_letters_dict[key]))
                writefile.write(letter)
        print("Letters have been created.\n")

    def load_data(self):
        pass

    def save_data(self):
        pass


if __name__ == "__main__":
    initial_dict = {"William Gates, III": [401321.52, 201342.71],
                        "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                        "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                        "Steve Ballmer": [5198.96, 654.98]}
    m = Mailroom(initial_dict)
    while True:
        try:
            print("Main Menu\n1. Load Data\n2. Save Data\n3. Send a Thank You\n4. Create a Report\n"
                  "5. Send Letters to All\n6. Quit")
            answer_dict = {"1": "Load Data",
                           "2": "Save Data",
                           "3": m.thank_you,
                           "4": m.create_report,
                           "5": m.send_letters,
                           "6": "quit"}
            answer = input("Please select an option. >")
            if answer == "1":
                with open("savefile.txt", "w") as file:
                    json_output = m.to_json_compat()
                    file.write(json_output)
            elif answer == "2":
                pass
            elif answer == "3":
                name = input("Please enter a full name. >")
                donation = input("Please enter a donation amount. >")
                m.donor_table_dict, print_string = answer_dict[answer](m.donor_table_dict, name,
                                                                          donation)
                print(print_string)
            elif answer == "4":
                m.donor_table_dict, print_string = answer_dict[answer](m.donor_table_dict)
                print(print_string)
            elif answer == "6" or answer == "quit":
                print("Have a nice day.")
                break
            else:
                answer_dict[answer](m.donor_table_dict)
        except KeyError:
            print()
