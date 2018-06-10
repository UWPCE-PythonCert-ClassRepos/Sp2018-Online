#!/usr/bin/env python3

'''

Author:     Eric Rosko
Lesson:     Session 8
Date:       june 4, 2018

These are the unit tests for my implementation of the mailroom class
in redis.

Usage: 1.) navigate into src/ first
python3 -m unittest unit-test.py -v
python3 -m unittest -v unit-test.py
python3 -m unittest unittest_mailroom_redis.MailroomRedisTests

'''

# from unittest import unittest
from unittest import TestCase
from mongodb_script import *
from login_database import *
import redis_script
import neo4j_script
import simple_script
import utilities
import json
import pickle
from mailroom_mongo import *

log = utilities.configure_logger('default', '../logs/unit-test.log')

class MailroomRedisTests(TestCase):

    def setUp(self):
        self.mailroom = MailroomMongo()
        r = login_database.login_redis_cloud()
        r.delete('bob')

    def tearDown(self):
        self.mailroom.wipe_database()

    def test_store_temporary_data(self):
        self.mailroom.store_temporary_data('bob', 'secret data')
        r = login_database.login_redis_cloud()
        secret = r.get("bob")
        self.assertEqual('secret data', secret)


    def test_retrieve_temporary_data(self):
        self.mailroom.store_temporary_data('bob', 'secret data')
        r = login_database.login_redis_cloud()
        secret = self.mailroom.retrieve_temporary_data('bob')
        self.assertEqual('secret data', secret)


if __name__ == "__main__":
    unittest.main()
