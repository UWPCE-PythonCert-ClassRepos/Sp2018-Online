#!/usr/bin/env python

import sys
import oo_mailroom as oo_mr

class Donor():

	def __init__(self, name):
		self.name = name
		self.donations = []

	@property
	def total_donations(self):
		return sum(self.donations)

	@property
	def number_of_donations(self):
		return(len(self.donations))

	@property
	def average_donation_size(self):
		return(self.total_donations/self.number_of_donations)

	def add_donation(self, amount):
		try:
			self.donations.append(float(amount))
		except ValueError:
			print("You must enter a numeric donation amount. ")



class DonorList():

	def __init__(self):
		self.donors = {}

	@property
	def donor_list(self):
		return(list(self.donors.keys()))

	# define a function to prompt the user for their desired action
	def prompt_user(self):
		print("Choose an action. ")
		print()
		print("1 - Send a thank you ")
		print("2 - Create a report ")
		print("3 - Send letters to everyone ")
		print("4 - Quit")

		while True:
			try:
				response = int(input(" > "))
			except ValueError:
				print("You must enter an *integer* value. ")
				continue
			else:
				return response

	def add_donor(self, new_donor):
		self.donors[new_donor.name] = new_donor

	def receive_thank_you_card_recepient_input(self):
		recipient = str(input("To whom would you like to send a thank you? > "))
		while recipient == "list":
			print(self.donor_list)
			print("\n")
			recipient = str(input("To whom would you like to send a thank you? > "))
		return(recipient)

	def receive_donation_amount(self):
		while True:
			donation_amount = input("How much would you like to donate? > ")
			try:
				donation_amount = float(donation_amount)
				if donation_amount < 0.00:
					print("You must enter a positive number to donate. ")
					continue
				break
			except ValueError:
				print("You must enter a numeric value. > ")
		return(donation_amount)

	def send_a_thank_you(self, out = sys.stdout):
		recipient = self.receive_thank_you_card_recepient_input()
		donation_amount = self.receive_donation_amount()
		self.donors.setdefault(recipient, Donor(recipient)).add_donation(donation_amount)
		out.write("Dear {:s}, \n".format(recipient))
		out.write("Thank you for your generous donations totaling ${:.2f}. \n".format(*[x.total_donations for i,x in enumerate(self.donors.values()) if x.name == recipient]))
		out.write("Best, The Donation Foundation")

	def create_a_report(self, out = sys.stdout):
		header_tuple = ("Donor Name", "Total Given", "Num Gifts", "Average Gift Size")
		out.write("{:20s} | {:10s} | {:10s} | {:15s}\n".format(*header_tuple))
		out.write("-"*70)
		out.write("\n")
		for donor in self.donors.values():
			out.write("{:20s} ${:10.2f}   {:10d}   ${:15.2f}\n".format(donor.name, donor.total_donations, donor.number_of_donations, donor.average_donation_size))

	def send_letters_to_everyone(self):
		for donor in self.donors.values():
			file = open("thank_you_{name:{width}}.txt".format(name=donor.name, width = len(donor.name)), "w")
			file.write("Dear {:s}, \n".format(donor.name))
			file.write("Thank you for your generous donations totaling ${:.2f}. \n".format(donor.total_donations))
			file.write("Best, The Donation Foundation")
			file.close()

if __name__ == '__main__':
	# Create a switch dictionary

	the_cb = Donor("Griffin")
	the_cb.add_donation(50)
	the_cb.add_donation(100)

	the_fs = Donor("Earl")
	the_fs.add_donation(50)
	the_fs.add_donation(200)

	the_rb = Donor("Carson")
	the_rb.add_donation(600)
	the_rb.add_donation(400)

	donor_list = DonorList()
	donor_list.add_donor(the_cb)
	donor_list.add_donor(the_fs)
	donor_list.add_donor(the_rb)

	switch_response_dictionary = {
	1: donor_list.send_a_thank_you,
	2: donor_list.create_a_report,
	3: donor_list.send_letters_to_everyone,
 	4: sys.exit
	}
	while True:
		try:
			switch_response_dictionary.get(donor_list.prompt_user())()
		except TypeError:
			print("You must enter a positive integer from one of 1, 2, 3, or 4.")
			continue







		












