#!/usr/bin/env python3
# -----------------------------------------------------------
# test_mailroom.py
#  uses unittest module to test mailroom.py program
# -----------------------------------------------------------

import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
import mailroom


class MailroomTest(unittest.TestCase):

    donor_data = [
        ('Al Donor1', [10.00, 20.00, 30.00, 40.00, 50.00]),
        ('Bert Donor2', [10.00]),
        ('Connie Donor3', [10.00, 10.00, 10.01]),
        ('Dennis Donor4', [10.00, 20.00, 20.00]),
        ('Egbert Donor5', [10.39, 20.21, 10.59, 4000.40]),
        ('Test DATA1', [1, 2, 3, 4, 5]),
        ('TestDATA2', [1, 2, 3]),
    ]

    def setUp(self):
        self.dl = mailroom.Donors()
        self.dl.DATA_FILE = 'test_donors.pkl'   # Create instance value for DATA_FILE to override class value
        # Note, with pickle, can't simply dl.load_donors(), as the pickle file was created from main() in the
        # mailroom module. So, we will simply build a database and save/load it from here.
        for don in self.donor_data:
            new_donor = self.dl.get_donor(don[0])
            for amt in don[1]:
                new_donor.add_donation(amt)

    def tearDown(self):
        # Removes files created by test_send_letters_all
        for filename in os.listdir('.'):
            if filename.endswith('.txt'):
                donorname = (filename[9:-4]).replace("_", " ")
                if donorname in self.dl.list_donors:
                    os.remove(filename)

    def test_save_data(self):
        self.assertEqual(7, self.dl.save_donorlist())

    def test_load_data(self):
        self.assertEqual(7, self.dl.load_donorlist())

    def test_donor_count(self):
        self.assertEqual(7, self.dl.count)

    def test_get_donor_names(self):
        for donor in self.dl.donorlist:
            self.assertIn(donor.last, donor.name)
            self.assertIn(donor.first, donor.name)

    def test_print_report(self):
        report_text = \
            '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Al Donor1                  $     150.00           5  $       30.00
Bert Donor2                $      10.00           1  $       10.00
Connie Donor3              $      30.01           3  $       10.00
Dennis Donor4              $      50.00           3  $       16.67
Egbert Donor5              $    4041.59           4  $     1010.40
Test DATA1                 $      15.00           5  $        3.00
TestDATA2                  $       6.00           3  $        2.00
'''
        f = StringIO()
        with redirect_stdout(f):
            self.dl.print_report()
        self.assertEqual(f.getvalue().strip(), report_text.strip())

    def test_generate_letter(self):
        for donor in self.dl.donorlist:
            format_string = donor.generate_letter()
            self.assertIn(donor.first, format_string)
            self.assertIn(donor.last, format_string)
            self.assertIn(str(donor.last_donation), format_string)  # Test donor's last donation is in letter

    def test_get_donor(self):
        self.assertIsNone(self.dl.get_donor(''))
        self.assertIsNotNone(self.dl.get_donor('Al Donor1'))
        pre_count = self.dl.count
        self.assertIsNotNone(self.dl.get_donor('NEW DONOR'))
        self.assertEqual(pre_count + 1, self.dl.count)

    def test_send_letters_all(self):
        f = StringIO()
        with redirect_stdout(f):
            self.dl.send_letters_all()
        for filename in os.listdir('.'):
            if filename.endswith('.txt'):
                donorname = (filename[9:-4]).replace("_", " ")
                self.assertIn(donorname, self.dl.list_donors)

    def test_donor_init(self):
        with self.assertRaises(ValueError):
            mailroom.Donor('')

    def test_donor_last_donation(self):
        c = mailroom.Donor('test')
        self.assertEqual(c.last_donation, None)
        with self.assertRaises(ValueError):
            c.add_donation(-100)
        c.add_donation(100)
        self.assertEqual(c.last_donation, 100.0)

if __name__ == "__main__":
   unittest.main()

