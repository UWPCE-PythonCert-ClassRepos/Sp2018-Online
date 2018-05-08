#!/usr/bin/env python3

from unittest import TestCase
import ballard as Gate


"""DATA"""
small_locke = 5
small_boats = 4

large_locke = 8
large_boats = 6

small_data = Gate.Locke(small_locke)
large_data = Gate.Locke(large_locke)

# Using small locke with large boats
erroneous_data = Gate.Locke(small_locke)


class BallardTest(TestCase):

    def test_small_normal(self):
        print("\n_________Starting small test__________ ")
        with small_data as SD:
            # Testing the data before moving the boats
            SD.enter_boat(small_boats)
            print("\nLeaving the ballards...!\n")

    def test_large_normal(self):
        print("\n_________Starting large test__________ ")
        with large_data as LD:
            LD.enter_boat(large_boats)
            print("\nLeaving the ballards...!\n")

    def test_errors(self):
        print("_________Starting Error test__________ ")
        with erroneous_data as ED:
            # The assert test runs ok
            self.assertRaises(ValueError, ED.enter_boat, 8)
            # Running the programming to show the raised error
            ED.enter_boat(large_boats)


if __name__ == 'main':
    TestCase()







