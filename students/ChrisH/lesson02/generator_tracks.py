#!/usr/bin/env python3
# -----------------------------------------------------------
# generator_tracks.py
#   Defines a generator that can be used to get all of the tracks
#   for a particular artist.
#   Uses the Spotify top 100 list for 2017 from a csv file
# -----------------------------------------------------------

import pandas as pd


music = pd.read_csv('featuresdf.csv')


def tracks_by_artist(artist):
    for track in [t[1] for t in zip(music.artists, music.name) if t[0] == artist]:
        yield track


def tracks_by_artist2(artist):
    for track in music.name.loc[music['artists'] == artist]:
        yield track


if __name__ == "__main__":
    a = tracks_by_artist("Ed Sheeran")
    for x in a:
        print(x)

    a = tracks_by_artist2("Ed Sheeran")
    for x in a:
        print(x)

"""
Ed Sheeran tracks:       
Shape of You
Castle on the Hill
Galway Girl
Perfect
"""
