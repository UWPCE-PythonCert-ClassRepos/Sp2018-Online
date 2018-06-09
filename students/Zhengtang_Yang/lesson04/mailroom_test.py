import unittest
import mailroom

class MailroomTest(unittest.TestCase):

	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Spiderman':[40,20],'Superman':[40,60,10]}
	
	def test_save_dec(self):
		temp1 = mailroom.Donors(self.donors)
		print(temp1)
		jc = temp1.to_json_compat()
		print(type(jc))

		# re-create it from the dict:
		temp2 = mailroom.Donors.from_json_dict(jc)
		self.assertEqual(temp1,temp2)
		print(temp1.to_json())

	def test_save_to_json(self):
		temp1 = mailroom.Donors(self.donors)
		print(temp1)
		temp1.add_donor('Hulk',10)
		temp1.save_json()
		temp2 = mailroom.Donors({'Batman':[100,50,30]})
		temp2.load_json()
		self.assertEqual(temp1.donors,temp2.donors)


if __name__ =="__main__":
	unittest.main()
