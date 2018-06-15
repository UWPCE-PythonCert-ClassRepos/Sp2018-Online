# from cursesmenu import SelectionMenu

import learn_data
import logging
import login_database
import utilities
import pprint

log = utilities.configure_logger('default', './logs/mailroom.log')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_database():
	donation_database = learn_data.get_donation_data()
	with login_database.login_mongodb_cloud() as client:
		log.info('Step 1: We are going to use a database called dev')
		log.info('But if it doesnt exist mongodb creates it')
		db = client['dev']

		log.info('And in that database use a collection called donation')
		log.info('If it doesnt exist mongodb creates it')

		donation = db['donation']

		log.info('Step 2: Now we add data from the dictionary above')
		donation.insert_many(donation_database)
		donation_dict = dict()
		for temp in donation.find():
			donation_dict[temp['name']] = temp['donation']  

	return donation, db, donation_dict

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
	for item in donors.find():
		pprint.pprint(item)

def add_donor(id0):
	d_amount = input("Enter a donation amount\n")
	with login_database.login_mongodb_cloud() as client:
		db = client['dev']
		donation = db['donation']
		temp = donation.find_one({'name':id0})
		if not temp:
			email_input = input('Input Email\n')
			donation.insert({'name': id0,
				'email': email_input,
				'donation': [int(d_amount),]
				})
		else:
			temp_list = temp['donation'].copy()
			temp_list.append(int(d_amount))
			donation.update_one({'name':id0},{'$set': {'donation': temp_list}})

def first_selection(donation):
	response = input("Enter Name or 'list' to see donor\n")
	if response == 'list':
		see_list(donation)
	else:
		add_donor(response)
		print(response + ', thank you for your donation.')

def second_selection(donors):
	report_gen(donors)

def third_selection(donors):
	letters(donors)

if __name__ == "__main__":
	donation, db, donation_dict = setup_database()
	a_list = ['Send a Thank You','Create a Report']
	selection_dict = {0: first_selection, 1: second_selection, 2: third_selection}
	while True: 
		print("""
			1. Send a Thank You
			2. Create a Report
			3. Send letter
			4. Exit
			""")
		selection = input("Enter Selection Number\n")
		if selection == '1':
			first_selection(donation) 
		elif selection == '2':
			second_selection(donation_dict)
		elif selection == '3':
			third_selection(donation_dict)
		elif selection == '4':
			db.drop_collection('donation')
			break
		else:
			print(type(selection))
			print('Please enter a number\n')
		input("Press Enter to continue...")