#!/usr/bin/env python3
"""
Assignment 02
1. Write a generator to find and print all of your favorite artist’s tracks from the data set.
2. Using the same data set, write a closure to capture high energy tracks.
"""
import pandas as pd

music = pd.read_csv("featuresdf.csv")

# Practice
# print(music.head())
# artists = music.artists
# print(artists)

# Generators
# Does "Ed Sheeran exist in the data?
artist = (a for a in music.artists if "Sheeran" in a)
print(next(artist))

songs = (name for artist, name in zip(music.artists, music.name) if "Sheeran" in artist)


# Iterate over the songs til the end - Results below done in iPython
# In [17]: next(songs)
# Out[17]: 'Shape of You'
#
# In [18]: next(songs)
# Out[18]: 'Castle on the Hill'
#
# In [19]: next(songs)
# Out[19]: 'Galway Girl'
#
# In [20]: next(songs)
# Out[20]: 'Perfect'

# iterate over using a for loop to avoid StopIteration:
# for song in songs:
#     print(song)
#
# In [21]: next(songs)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-21-2b7b6b5d1143> in <module>()
# ----> 1 next(songs)
#
# StopIteration:

# Closures


# Make a closure to find high energy tracks over 0.8 in the music.energy column
def find_high_energy_track(level):
    def energy_level(energy):
        return energy > level

    return energy_level


# Call our function with the desired level criteria
energy = find_high_energy_track(0.8)

t = ((a, n, e) for (a, n, e) in zip(music.artists, music.name, energy(music.energy)))
next(t)
next(t)
next(t)
next(t)

# Below is output from running the above to capture the energy level above 0.8
# Not run to completion
# In [18]: next(t)
# Out[18]: ('Ed Sheeran', 'Shape of You', False)
#
# In [19]: next(t)
# Out[19]: ('Luis Fonsi', 'Despacito - Remix', True)
#
# In [20]: next(t)
# Out[20]: ('Luis Fonsi', 'Despacito (Featuring Daddy Yankee)', False)
#
# In [21]: next(t)
# Out[21]: ('The Chainsmokers', 'Something Just Like This', False)
#
# In [22]: next(t)
# Out[22]: ('DJ Khaled', "I'm the One", False)
#
# In [23]: next(t)
# Out[23]: ('Kendrick Lamar', 'HUMBLE.', False)
#
# In [24]: next(t)
# Out[24]: ('Kygo', "It Ain't Me (with Selena Gomez)", False)

# Running a for loop on t to see all the tracks with the energy level above 0.8
# Need to do define it again since previously ran next() on t
t = ((a, n, e) for (a, n, e) in zip(music.artists, music.name, energy(music.energy)))
for track in t:
    print(track)

