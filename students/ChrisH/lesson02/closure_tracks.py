#!/usr/bin/env python3
# -----------------------------------------------------------
# generator_tracks.py
#   Defines a generator that can be used to get all of the tracks
#   for a particular artist.
#   Uses the Spotify top 100 list for 2017 from a csv file
# -----------------------------------------------------------

import pandas as pd


def tracks_by_energy(filename='featuresdf.csv'):
    music = pd.read_csv(filename)

    def tracks_energy(energy):
        nonlocal music
        return [t for t in sorted(zip(music.artists, music.name, music.energy)) if t[2] > energy]

    return tracks_energy


if __name__ == "__main__":

    tbe = tracks_by_energy('featuresdf.csv')

    for song in tbe(0.8):
        print("{}    {}    {:3n}".format(*song))


