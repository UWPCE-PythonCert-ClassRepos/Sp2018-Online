#!/usr/bin/env python3

'''
Name:       homework02.py
Author:     Eric Rosko
Date:       Apr 15, 2018
Python ver. 3.6.5
'''

import pandas as pd
from pprint import pprint
from collections import namedtuple

# global list to contain songs
g_songs = []


def iternamedtuples(df):
    Row = namedtuple('Song', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])


def filterByDanceabilityAndLoudness():
    music = pd.read_csv("featuresdf.csv")
    named_tuples = iternamedtuples(df)
    both = filter(lambda x: x.danceability > 0.8 and x.loudness < -5.0, named_tuples)
    sortedItems = sorted(tuple(both), key=lambda x: x.danceability, reverse = True)

    myList = list()
    for i in sortedItems:
        temp = (i.artists, i.name)
        myList.append(temp)
    return myList


def generateSheeran(music):
    named_tuples = iternamedtuples(music)
    for t in named_tuples:
        if t.artists == "Ed Sheeran":
            yield((t.artists, t.name))


def closure():
    global g_songs
    def findEnergyTracks(_data):
        assert _data is not None
        # print("calling findEnergyTracks")
        for index, row in _data.iterrows():
            if row['energy'] > 0.8:
                g_songs.append((row['name'], row['artists'], row['energy']))
    return findEnergyTracks


def filter_with_closure():
    music = pd.read_csv("featuresdf.csv")
    func = closure()
    func(music)

    # sorts in-place
    g_songs.sort(key = lambda a: a)


def favorite_artist():
    music = pd.read_csv("featuresdf.csv")
    named_tuples = tuple(generateSheeran(music))
    # print(named_tuples)
    return named_tuples
