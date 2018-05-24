#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 01 - Comprehension Music csv file - Unitest
    SUB TITLE: Functional Programming - Comprehension - Pandas csv files
      CREATOR: PydPiper
 DATE CREATED: 4/10/18
LAST MODIFIED: 4/10/18
  DESCRIPTION: Test each functional def
********************************************************************************************************************"""

"""IMPORTS"""
import unittest
import comprehension_music as cm
import pandas as pd

"""GLOBAL DATA"""
bad_csv_no_artists = pd.DataFrame(data=[["art1", "name1", "0.9", "-5"]],
                                 columns=["no_artists", "name", "danceability", "loudness"])
bad_csv_no_name = pd.DataFrame(data=[["art1", "name1", "0.9", "-5"]],
                               columns=["artists", "no_name", "danceability", "loudness"])
bad_csv_no_dance = pd.DataFrame(data=[["art1", "name1", "0.9", "-5"]],
                                columns=["artists", "name", "no_danceability", "loudness"])
bad_csv_no_loudness = pd.DataFrame(data=[["art1", "name1", "0.9", "-5"]],
                                   columns=["artists", "name", "danceability", "no_loudness"])
bad_csv_data1 = pd.DataFrame(data=[["art1", "name1", "not_int", "-5"]],
                             columns=["artists", "name", "danceability", "loudness"])
bad_csv_data2 = pd.DataFrame(data=[["art1", "name1", "0.9", "not_int"]],
                             columns=["artists", "name", "danceability", "loudness"])
# art 1-6 is good data, 6th is not in top5, 7,8 are bad and should not be logged
test_dict = {"artists": ["art1", "art2", "art3", "art4", "art5", "art6", "art7", "art8"],
             "name": ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8"],
             "danceability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.2, 0.9],
             "loudness": [-6, -6, -6, -6, -6, -6, -6, -1]}
test_csv = pd.DataFrame.from_dict(test_dict)


"""TEST"""


class MyTest(unittest.TestCase):
    def test_file_bad(self):
        wrong_file = "these are not the drones"
        with self.assertRaises(FileNotFoundError):
            cm.read_file(wrong_file)

    def test_file_good(self):
        right_file = "featuresdf.csv"
        self.assertTrue(type(cm.read_file(right_file)) == pd.DataFrame)

    def test_check_the_checker_artists(self):
        with self.assertRaises(Exception):
            cm.data_check(bad_csv_no_artists)

    def test_check_the_checker_name(self):
        with self.assertRaises(Exception):
            cm.data_check(bad_csv_no_name)

    def test_check_the_checker_dance(self):
        with self.assertRaises(Exception):
            cm.data_check(bad_csv_no_dance)

    def test_check_the_checker_loudness(self):
        with self.assertRaises(Exception):
            cm.data_check(bad_csv_no_loudness)

    def test_check_the_checker_bad_dance(self):
        # data check for number conversion in pandas via numpy
        with self.assertRaises(ValueError):
            cm.data_check(bad_csv_data1)

    def test_check_the_checker_bad_loudness(self):
        with self.assertRaises(ValueError):
            cm.data_check(bad_csv_data2)

    def test_data_strip_dance(self):
        # fed a DataFrame, should return stripped dict, dance > 0.8, loud < -5.0
        new_dict = cm.data_strip(test_csv)
        for values in new_dict["danceability"]:
            self.assertGreater(values, 0.8)

    def test_data_strip_loudness(self):
        # fed a DataFrame, should return stripped dict, dance > 0.8, loud < -5.0
        new_dict = cm.data_strip(test_csv)
        for values in new_dict["loudness"]:
            self.assertLess(values, -5)

    def test_sort_len_artists(self):
        # return top 5, based on highest danceability
        new_dict = cm.data_strip(test_csv)
        l_artists, l_songs = cm.sort_special(new_dict)
        self.assertEqual(5, len(l_artists))

    def test_sort_len_songs(self):
        # return top 5, based on highest danceability
        new_dict = cm.data_strip(test_csv)
        l_artists, l_songs = cm.sort_special(new_dict)
        self.assertEqual(5, len(l_songs))

    def test_sort_top1_artist(self):
        # return top 5, based on highest danceability
        new_dict = cm.data_strip(test_csv)
        l_artists, l_songs = cm.sort_special(new_dict)
        self.assertEqual("art1", l_artists[0])

    def test_sort_top1_song(self):
        # return top 5, based on highest danceability
        new_dict = cm.data_strip(test_csv)
        l_artists, l_songs = cm.sort_special(new_dict)
        self.assertEqual("name1", l_songs[0])


"""MAIN"""
if __name__ == "__main__":
    unittest.main()
