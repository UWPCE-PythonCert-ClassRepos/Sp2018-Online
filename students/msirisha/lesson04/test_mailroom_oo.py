import unittest
from mailroom_oo import Donors, Donor
from contextlib import redirect_stdout
from io import StringIO
import os


class MailroomOoUnitTests(unittest.TestCase):
    donor_data = {"sai emani": [20.23, 30.456, 50.786],
                  "sirisha marthy": [67.89, 45.89],
                  "ani emani": [12.789, 5.456],
                  "charles dickens": [15.89, 89.20, 345.67],
                  "mark twain": [678.986]
                  }

    def setUp(self):
        self.donors = Donors()
        for donor in self.donor_data:
            dnr = self.donors.get_donor(donor)
            for amt in self.donor_data[donor]:
                dnr.add_donation(amt)

    def test_donors_count(self):
        self.assertEqual(5, self.donors.count)

    def test_load_donors_list(self):
        self.assertEqual(5, self.donors.load_donors_list())

    def test_save_donors_list(self):
        self.assertEqual(5, self.donors.save_donors_list())

    def test_add_donor(self):
        new_donor = self.donors.get_donor("first last")
        self.assertEqual(6, self.donors.count)
        self.assertEqual("first last", self.donors.list_of_donors[-1])
        self.assertEqual("first last", new_donor.name)

    def test_list_of_donors(self):
        donors_list = ['sai emani', 'sirisha marthy', 'ani emani', 'charles dickens', 'mark twain']
        self.assertEqual(self.donors.list_of_donors, donors_list)

    def test_create_a_report(self):
        expected = \
        '''
Donor Name                | Total Given | Num Gifts | Average Gift
sai emani                  $     101.47           3 $       33.82
sirisha marthy             $     113.78           2 $       56.89
ani emani                  $      18.25           2 $        9.12
charles dickens            $     450.76           3 $      150.25
mark twain                 $     678.99           1 $      678.99
        '''

        f = StringIO()
        with redirect_stdout(f):
            self.donors.create_a_report()
        self.assertEqual(f.getvalue().strip(), expected.strip())

    def test_generate_letter(self):
        for donor in self.donors.donors_list:
            f_string = donor.generate_letter()
            self.assertIn(donor.first_name, f_string)
            self.assertIn(donor.last_name, f_string)
            self.assertIn(str(donor.latest_donation), f_string)

    def test_send_letters(self):
        f = StringIO()
        with redirect_stdout(f):
            self.donors.send_letters()
        for filename in os.listdir('.'):
            if filename.endswith('.txt'):
                donor_name = filename[0:-4]
                self.assertIn(donor_name, self.donors.list_of_donors)

    def test_latest_donation(self):
        latest_donation_of_first_donor = self.donors.donors_list[0].latest_donation
        self.assertEqual(latest_donation_of_first_donor, 50.786)

    def test_add_donation(self):
        test_obj = Donor("test")
        self.assertEqual(test_obj.latest_donation, None)
        with self.assertRaises(ValueError):
            test_obj.add_donation(-10)
        test_obj.add_donation(10)
        self.assertEqual(test_obj.latest_donation, 10)

    def test_donor_init(self):
        with self.assertRaises(ValueError):
            test_obj = Donor(None)

    def tearDown(self):
        for filename in os.listdir():
            donor_name = filename[0:-4]
            if filename.endswith('.txt') and donor_name in self.donors.list_of_donors:
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()
