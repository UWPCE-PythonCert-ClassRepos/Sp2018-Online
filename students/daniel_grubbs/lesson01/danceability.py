#!/usr/bin/env python3
"""
Get artists and song names for for tracks with danceability scores over 0.8 and loudness scores below -5.0.
In other words, quiet yet danceable tracks. Also, these tracks should be sorted in descending order by danceability
so that the most danceable tracks are up top. You should be able to work your way there starting with the
comprehension above. And while you could use Pandas features along the way, you don’t need to. To accomplish the
objective you do not need to know anything more about Pandas than what you can infer from the material herein.
Standard library functions that could come in handy include zip() and sorted().

"""
import pandas as pd

music = pd.read_csv("featuredf.csv")

# Become familiar with the geneal shape of the data
# music.head()
# music.describe()
#
# [x for x in music.danceability if x > 0.8]
print("Practice using sorted() and reverse=True\n")
[(a, d) for (a, d) in zip(music.artists, music.danceability) if y > 0.8]
sorted([(a, d) for (a, d) in zip(music.danceability, music.artists) if d > 0.8], reverse=True)

# Create a function to use as a key when using sorted()
print("\nPractice using a function that can be used as a key in sorted()\n")


def danceability_sorted_desc(songs):
    """Sort the input in descending order."""
    return -songs[1]


sorted([(a, d) for (a, d) in zip(music.artists, music.danceability) if d > 0.8], key=danceability_sorted_desc)

# Return the artists and song for tacks with danceability scores over 0.8 and loudness scores below -5.0
# Needed: music.artists, music.name, music.danceability, music.loudness
# Change the function used for key in sorted to reflect the new position of music.danceability
print("\nPulling things together and meeting the requirements for the task.\n")


def danceability_sorted_desc(songs):
    """Sort the input in descending order."""
    return -songs[2]


sorted([(a, n, d, l) for (a, n, d, l) in zip(music.artists, music.name, music.danceability, music.loudness)
        if d > 0.8 and l < -5.0], key=danceability_sorted_desc)

