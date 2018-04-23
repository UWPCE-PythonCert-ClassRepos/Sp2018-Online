#!/usr/bin/python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 02 - Assignment
     SUB TITLE: Generator/Closures Music
       CREATOR: PydPiper
  DATE CREATED: 4/14/18
 LAST MODIFIED: 4/15/18
   DESCRIPTION: Read in the given csv file. Get artists, song name, and energy.
                1) Write a generator that finds all the tracks for a input artist
                if the artist doesnt doesnt exist, print out Ed Sheeran's tracks
                2) Write a closure that looks for tracks with energy > 8.0
                print out artist / track / energy level
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
    Checks for "energy", "artist" and "name column headers, and its data type under it.
    :param data_csv: pandas.core.frame.DataFrame
    :return: none, or raises an error
    """

    # the following headers are used in this script, therefore they must exist
    header_check = ["energy", "artists", "name"]
    for header in header_check:
        try:
            dummy = data_csv.eval(header)[0]
        # DataFrame.attribute raises a AttributeError, however DataFrame.eval(no_att_name) raises a pandas.UndefinedVar
        except:
            raise AttributeError(f"{header} is column was not found in csv file")

    detail_check = ["energy"]
    for header in detail_check:
        for i, x in enumerate(data_csv.eval(header), 2):
            try:
                dummy = float(x)
            except ValueError:
                raise ValueError(f"{header} on row {i}={x} cannot be converted to a integer/float")


def find_mytracks(myartist, data_csv):
    """
    Generator; Produces track names for an artist passed in. State is kept as an instance, called via next
    :param myartist: str, artists name. If artists is not in data, "Ed Sheeran" tracks are yielded
    :yield: str, track names
    """
    if myartist in list(data_csv.artists):
        for i, artist in enumerate(data_csv.artists):
            if artist == myartist:
                yield data_csv.name[i]
    else:
        print("Artist not on file, try a track from Ed Sheeran:")
        for i, artist in enumerate(data_csv.artists):
            if artist == "Ed Sheeran":
                yield data_csv.name[i]


def find_myenergy():
    """
    Closure; Returns Energy / Artists / Tracks that have > .8 energy rating
    :return: None, Closure prints internally
    """
    mylocalenergy = 0.8

    def lookup(myenergy=mylocalenergy):
        print("{:<7}|{:<20}|{:^50}".format("Energy", "Artist", "Track"))
        for i, energy in enumerate(data_csv.energy):
            if energy > myenergy:
                print(f"{data_csv.energy[i]:^7.3f}|{data_csv.artists[i]:<20}|{data_csv.name[i]:<50}|")
        return None
    return lookup


"""MAIN"""
if __name__ == "__main__":
    # Runtime -h description
    parser = ArgumentParser(description="1) List tracks by artists (via function: find_mytracks(artist)"
                                        "2) List of high energy track (via function: find_myenergy()"
                                        "Data Source: featuresdf.csv",)
    parser.add_argument("--artist", default="Ed Sheeran", type=str)
    args = parser.parse_args()

    data_csv = read_file("featuresdf.csv")
    data_check(data_csv)

    print(f"Tracks for {args.artist}:")
    instance = find_mytracks(args.artist, data_csv)
    while True:
        try:
            print(next(instance))
        except StopIteration:
            break

    print("\nSuggested High Energy Tracks:")
    high_eng_track = find_myenergy()
    high_eng_track()

