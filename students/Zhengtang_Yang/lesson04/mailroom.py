# from cursesmenu import SelectionMenu
import json_save.json_save_dec as js

@js.json_save
class Donors:

	donors = js.Dict()

	def __init__(self, donors_dict):
		self.donors = donors_dict

	def __iter__(self):
		return iter(self.donors)

	def __contains__(self,donor_str):
		return donor_str in self.donors.keys()

	def report_gen(self):
		header = ('Donor Name','Total Given','Num Gifts','Average Gift')
		row_format, row_format0 = '{:<14}','{:<14}'
		for item in header[1:]:
			row_format += f' | {{:>{len(item)}}}'
			row_format0 += f'  {{}}{{:>{len(item)}}}'
		print(row_format.format(*header))
		print('-'*len(row_format.format(*header)))
		for item in self.donors.keys():
			print(row_format0.format(item,'$',sum(self.donors[item]),' ', len(self.donors[item]),'$',round(sum(self.donors[item])/len(self.donors[item]),1)))

	def letters(self):
		for names in self.donors.keys():
			with open(f'{names}.txt','w') as text_file:
				print(f'Dear {names},\nThank you for your very kind donation of ${sum(self.donors[names])}.\nIt will be put to very good use.\nSincerely,\n-The Team', file=text_file)

	def see_list(self):
		for item in self.donors.keys():
			print(item)

	def add_donor(self, name_str, amount):
		try:
			if name_str in self.donors:
				self.donors[name_str].append(int(amount))
			else:
				self.donors[name_str] = [int(amount)]
		except ValueError:
			print("Please Enter a number.")

	def challenge(self, name_str, factor, min_donation=0, max_donation=None):
		temp = list(set(self.filter_min(min_donation)).intersection(self.filter_max(max_donation)))
		amount0 = sum(map(lambda x: sum(self.donors[x])*factor, temp))
		self.add_donor(name_str, amount0)

	def filter_min(self, min_donation):
		return list(filter(lambda x: sum(donors[x]) > min_donation, self.donors.keys()))

	def filter_max(self, max_donation):
		if max_donation == None:
			return self.donors.keys()
		else:
			return list(filter(lambda x: sum(donors[x]) < max_donation, self.donors.keys()))

	def load_json(self):
		with open("save_file.json") as file_in:
			temp = js.from_json(file_in)
		self.donors = temp.donors

	def save_json(self):
		json_dlist = self.to_json()
		with open("save_file.json", 'w') as file_out:
			file_out.write(json_dlist)

def first_selection(donors_obj):
	response = input("Enter a Full Name or 'list' to see donor\n")
	if response == 'list':
		donors_obj.see_list()
	else:
		d_amount = input("Enter a donation amount\n")
		donors_obj.add_donor(response, d_amount)
		print(response + ', thank you for your donation.')

def second_selection(donors_obj):
	donors_obj.report_gen()

def third_selection(donors_obj):
	donors_obj.letters()

if __name__ == "__main__":
	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Hulk':[10],'Spiderman':[40,20],'Superman':[40,60,10]}
	temp = Donors(donors)
	# a_list = ['Send a Thank You','Create a Report','Send letters to everyone']
	# selection_dict = {0: first_selection, 1: second_selection, 2: third_selection}
	# while True: 
	# 	selection = SelectionMenu.get_selection(a_list)
	# 	if selection == 3:
	# 		break
	# 	selection_dict.get(selection)(temp)
	# 	input("Press Enter to continue...")