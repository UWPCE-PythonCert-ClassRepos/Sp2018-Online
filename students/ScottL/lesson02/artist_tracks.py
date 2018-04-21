#!/usr/bin/env python

#-------------------------------------------------#
# Title: artist_tracks
# Dev: Scott Luse
# Date: April 15, 2018
#-------------------------------------------------#

"""
generators and closure using featuresdf.csv

1. Write a generator to find and print all of your favorite artist’s tracks from the data set.
Your favorite artist isn’t represented in that set? In that case, find Ed Sheeran tracks.

2. Load the data set following the instructions from last week.
Submit your generator expression and the titles of Ed’s tracks.

3. Using the same data set, write a closure to capture high energy tracks.
We will define high energy tracks as anything over 0.8 (not typo 8.0).
Submit your code and the tracks it finds, artist name, track name and energy value.

"""


import pandas as pd

def music_artist(artist, music):
    '''
    Specific artist music list from Generator
    '''
    for (x, y) in zip(music.name, music.artists):
        if y == artist:
            yield x


def danceability(artist, music):
    '''
    Specific artist music list using last week's Comprehension method
    '''

    list1 = sorted([(w,x,y,z) for (w,x,y,z) in zip(music.name, music.artists, music.danceability, music.loudness)
                    if x == artist], reverse=False)
    return(list1)


def set_energy_music(music):
    '''
    High energy music list using closure
    '''
    def music_level(num):
        for (x, y, z) in zip(music.name, music.artists, music.energy):
            if z >= num:
                yield x + ", " + y + ", " + str(round(z,3))
    return music_level


def main():
    print("\n" + "Loading data set...")
    music = pd.read_csv("featuresdf.csv")
    favorite_music = music_artist("Ed Sheeran", music)

    print("\n"+"Generator: Ed Sheeran’s tracks")
    print("=====================================")
    for i in favorite_music:
        print(i)

    print("\n"+"Comprehension: Ed Sheeran’s tracks")
    print("=====================================")
    good_music = danceability("Ed Sheeran", music)
    for i in good_music:
        print(i)

    print("\n"+"Closure: High energy tracks")
    print("TRACK, ARTIST, ENERGY LEVEL")
    print("=====================================")
    f = set_energy_music(music)
    #print(list(f(0.8)))
    for i in list(f(0.8)):
        print(i)


if __name__ == "__main__":
    main()

