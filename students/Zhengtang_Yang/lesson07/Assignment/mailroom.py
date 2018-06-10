# from cursesmenu import SelectionMenu

import logging
from peewee import *
from mailroom_model import Donor, Donation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def report_gen(donors):
	header = ('Donor Name','Total Given','Num Gifts','Average Gift')
	row_format, row_format0 = '{:<14}','{:<14}'
	for item in header[1:]:
		row_format += f' | {{:>{len(item)}}}'
		row_format0 += f'  {{}}{{:>{len(item)}}}'
	print(row_format.format(*header))
	print('-'*len(row_format.format(*header)))
	for item in donors.keys():
		print(row_format0.format(item,'$',sum(donors[item]),' ', len(donors[item]),'$',round(sum(donors[item])/len(donors[item]),1)))

def letters(donors):

	for names in donors.keys():
		with open(f'{names}.txt','w') as text_file:
			print(f'Dear {names},\nThank you for your very kind donation of ${sum(donors[names])}.\nIt will be put to very good use.\nSincerely,\n-The Team', file=text_file)

def see_list(donors):
	for item in donors.keys():
		print(item)

def add_donor(id0, amount, donors):
	database = SqliteDatabase('./data/mailroom.db')
	temp = input('Enter name\n')
	with database.transaction():
		new_donor = Donor(name = temp, _id_ = id0)
		new_donor.save(force_insert=True)
		new_donation = Donation(amount = amount, donor = id0)
		new_donation.save()
	# try:
	# 	if name_str in self.donors:
	# 		self.donors[name_str].append(int(amount))
	# 	else:
	# 		self.donors[name_str] = [int(amount)]
	# except ValueError:
	# 	print("Please Enter a number.")

def first_selection(donors):
	response = input("Enter UserID or 'list' to see donor\n")
	if response == 'list':
		see_list(donors)
	else:
		d_amount = input("Enter a donation amount\n")
		add_donor(response, d_amount, donors)
		print(response + ', thank you for your donation.')

def second_selection(donors):
	report_gen(donors)

def third_selection(donors):
	letters(donors)

def db2dict():
	query = Donation.select(Donor, Donation).join(Donor)
	dict0 = dict()
	for d in query:
		if d.donor.name in dict0:
			dict0[d.donor.name].append(d.amount)
		else:
			dict0[d.donor.name] = [d.amount,]
	return dict0


if __name__ == "__main__":
	a_list = ['Send a Thank You','Create a Report']
	selection_dict = {0: first_selection, 1: second_selection, 2: third_selection}
	while True: 
		dict0 = db2dict()
		print("""
			1. Send a Thank You
			2. Create a Report
			3. Send letter
			4. Exit
			""")
		selection = input("Enter Selection Number\n")
		if selection == '1':
			first_selection(dict0) 
		elif selection == '2':
			second_selection(dict0)
		elif selection == '3':
			third_selection(dict0)
		elif selection == '4':
			break
		else:
			print(type(selection))
			print('Please enter a number\n')
		input("Press Enter to continue...")