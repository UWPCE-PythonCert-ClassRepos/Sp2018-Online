#!/usr/bin/python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 01 - Comprehension Music csv file
    SUB TITLE: Functional Programming - Comprehension - Pandas csv files
      CREATOR: PydPiper
 DATE CREATED: 4/8/18
LAST MODIFIED: 4/10/18
  DESCRIPTION: Read in the given csv file. Get artists and song names for tracks with danceability scores over 0.8
               and loudness scores below -5.0. Sort by descending order of danceability. List the top 5 tracks.
********************************************************************************************************************"""

"""IMPORTS"""
from pandas import read_csv
from os import getcwd
from argparse import ArgumentParser


"""FUNCTIONS"""
def read_file(file_name):
    """
    Takes a .csv filename and loads it into memory via pandas.read_csv(filename)
    :param file_name: string
    :return: data_csv pandas.core.frame.DataFrame
    """
    while True:
        try:
            data_csv = read_csv(file_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"{file_name} not found in current directory: \n ({getcwd()})")
        else:
            break
    return data_csv


def data_check(data_csv):
    """
    Checks for "danceability", "loudness", "artist" and "name column headers, and its data type under it.
    :param data_csv: pandas.core.frame.DataFrame
    :return: none, or raises an error
    """

    # the following headers are used in this script, therefore they must exist
    header_check = ["danceability", "loudness", "artists", "name"]
    for header in header_check:
        try:
            dummy = data_csv.eval(header)[0]
        # DataFrame.attribute raises a AttributeError, however DataFrame.eval(no_att_name) raises a pandas.UndefinedVar
        except:
            raise AttributeError(f"{header} is column was not found in csv file")

    detail_check = ["danceability", "loudness"]
    for header in detail_check:
        for i, x in enumerate(data_csv.eval(header)):
            try:
                dummy = float(x)
            except ValueError:
                raise ValueError(f"{header} on row {i+1}={x} cannot be converted to a integer/float")


def data_strip(data_csv):
    """
    Takes a pandas core.series object and based on condition_strip() it down-selects data
    :param data_csv: pandas.core.frame.DataFrame
    :return: dictionary
    """
    # down-select data from csv
    data_base = {}
    for headers in data_csv.columns:
        cur_column = data_csv.get(headers)
        data_base.update({headers: [cur_column[i] for i in range(len(cur_column)) if cond_strip(i, data_csv)]})
    return data_base

def cond_strip(iterable_index, data_csv):
    """
    Data down-selection logic. danceability > 0.8 and loudness < -5.0
    :param iterable_index: int
    :param data_csv: pandas.core.frame.DataFrame
    :return: Bool
    """
    if list(data_csv.danceability)[iterable_index] > 0.8:
        if list(data_csv.loudness)[iterable_index] < -5.0:
            return True
    else:
        return False

def sort_special(data_base):
    """
    Takes the data_base dictionary and down-selects only the top 5 danceable content
    :param data_base: dictionary
    :return: artist_list, songs_list
    """

    l_artists = data_base["artists"]
    l_name = data_base["name"]
    l_dance = data_base["danceability"]

    # sorted_out[0] = artists, [1] = songs, [2] = danceablility
    sorted_out = sorted(zip(l_artists, l_name, l_dance), key=lambda x: x[2], reverse=True)
    # only return top 5
    return [items[0] for items in sorted_out[:5]], [items[1] for items in sorted_out[:5]]

"""MAIN"""
if __name__ == "__main__":
    # Runtime -h description
    parser = ArgumentParser(description="Script to downselect top 5 tracks out of a featuresdf.csv")
    args = parser.parse_args()

    data_csv = read_file("featuresdf.csv")
    data_check(data_csv)
    data_base = data_strip(data_csv)
    l_artists, l_songs = sort_special(data_base)

    print("Top 5 Danceable and proper loudness tracks:\n")
    for index in range(len(l_artists)):
        print(f"#{index+1} Artists/Song: {l_artists[index]} / {l_songs[index]}")
