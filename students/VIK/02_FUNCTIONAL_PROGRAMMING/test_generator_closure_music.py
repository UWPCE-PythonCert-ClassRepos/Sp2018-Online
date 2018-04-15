#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 02 - Assignment
    SUB TITLE: Unit Test
      CREATOR: PydPiper
 DATE CREATED: 4/14/18
LAST MODIFIED: 4/15/18
  DESCRIPTION: Test each functional def
********************************************************************************************************************"""

"""IMPORTS"""
import unittest
import generator_closure_music as gc
import pandas as pd


"""GLOBAL DATA"""
bad_csv_no_artists = pd.DataFrame(data=[["art1", "name1", "0.9"]],
                                 columns=["no_artists", "name", "energy"])
bad_csv_no_name = pd.DataFrame(data=[["art1", "name1", "0.9"]],
                               columns=["artists", "no_name", "energy"])
bad_csv_no_energy = pd.DataFrame(data=[["art1", "name1", "0.9"]],
                                columns=["artists", "name", "no_energy"])
bad_csv_data1 = pd.DataFrame(data=[["art1", "name1", "not_int"]],
                             columns=["artists", "name", "energy"])
# test data, energy filter check
test_dict = {"artists": ["art1", "art1", "Ed Sheeran", "Ed Sheeran"],
             "name": ["name1", "name2", "Ed's track 1", "Ed's track 2"],
             "energy": [0.2, 0.8, 0.9, 0.2]}
test_csv = pd.DataFrame.from_dict(test_dict)


"""TEST"""
class MyTest(unittest.TestCase):
    def test_file_bad(self):
        wrong_file = "these are not the drones"
        with self.assertRaises(FileNotFoundError):
            gc.read_file(wrong_file)

    def test_file_good(self):
        right_file = "featuresdf.csv"
        self.assertTrue(type(gc.read_file(right_file)) == pd.DataFrame)

    def test_check_the_checker_artists(self):
        with self.assertRaises(Exception):
            gc.data_check(bad_csv_no_artists)

    def test_check_the_checker_name(self):
        with self.assertRaises(Exception):
            gc.data_check(bad_csv_no_name)

    def test_check_the_checker_energy(self):
        with self.assertRaises(Exception):
            gc.data_check(bad_csv_no_energy)

    def test_check_the_checker_bad_energy(self):
        # data check for number conversion in pandas via numpy
        with self.assertRaises(ValueError):
            gc.data_check(bad_csv_data1)

    def test_data_find_tracks(self):
        # fed a DataFrame, should return all the names for given artist on the data
        instance = gc.find_mytracks(test_csv.artists[0], test_csv)
        i = 0
        while True:
            try:
                track = next(instance)
            except StopIteration:
                break
            else:
                self.assertEqual(test_csv.name[i], track)
                i += 1

    def test_data_find_noartist_tracks(self):
        # fed a DataFrame, should return all the names for "Ed Sheeran given an artist not on data
        instance = gc.find_mytracks("random_artist", test_csv)
        i = 0
        while True:
            try:
                track = next(instance)
            except StopIteration:
                break
            else:
                self.assertEqual(test_csv.name[2+i], track)
                i += 1

"""MAIN"""
if __name__ == "__main__":
    unittest.main()
