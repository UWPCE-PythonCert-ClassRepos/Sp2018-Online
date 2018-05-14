#!/usr/bin/env python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 04 - Activity - Unittest
     SUB TITLE: Mailroom - Metaprogramming
       CREATOR: PydPiper
  DATE CREATED: 4/28/18
 LAST MODIFIED: 5/5/18
   DESCRIPTION: Convert the 210 mailroom programming's database into JSON save/load format via metaprogramming
********************************************************************************************************************"""

"""IMPORTS"""
import unittest
import mailroom as mail

"""TEST DATA"""
json_data = {'Tony Stark': [906.04, 2], 'Captain America': [4500.0, 2], 'Daisy Johnson': [14.97, 3], 'Melinda May': [555.02, 2], 'Phil Coulson': [9999.99, 1]}


class MyTest(unittest.TestCase):
    def test_to_json_compat(self):
        self.assertEqual(mail.data_base.to_json_compat()['data'], json_data)

    def test_to_json(self):
        with open('json_out', "r") as f:
            content = f.read()
            self.assertEqual(content, mail.data_base.to_json())


if __name__ == "__main__":
    unittest.main()
