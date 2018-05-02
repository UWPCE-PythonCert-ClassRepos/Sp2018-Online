#!/usr/bin/env python

import json_save_mailroom as jsm
import unittest

class json_save_mailroom_test(unittest.TestCase):
	# test boat threshold if number of boats exceeds locke size
    def test_save_to_json(self):

        # create a donor
        the_cb = jsm.Donor("Griffin")
        the_cb.add_donation(50)
        the_cb.add_donation(100)
        
        # create and populate a donor list
        donor_list = jsm.DonorList({})
        donor_list.add_donor(the_cb)

        # create a JSON compatable donor list
        jc = donor_list.to_json_compat()

        # create a second donor list from the JSON compatable donor list created above
        donor_list2 = donor_list.from_json_dict(jc)

        # test that the two lists are equal
        self.assertEqual(donor_list, donor_list2)

if __name__ == '__main__':
    unittest.main() 