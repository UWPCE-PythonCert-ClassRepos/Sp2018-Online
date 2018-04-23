#!/usr/bin/env python

import pandas as pd
import operator

# read music in as pandas data frame
music = pd.read_csv("/Users/davidrusso/Documents/Classes/Python Certificate/Advanced Python/Sp2018-Online/students/david_russo/lesson02/featuresdf.csv", encoding = "ISO-8859-1")
print("The csv has been read, it has {:d} rows.".format(len(music)))

music.groupby(['artists']).size()

# Write a generator to find and print all of your favorite artist’s tracks from the data set
# My favorite artist for this exercise is Drake

def find_drake():
    song_index = 0
    while song_index < len(music):
        if music['artists'][song_index] == 'Drake':
            yield music['name'][song_index]
        song_index += 1

drake_tracks = find_drake()


# write each song to text
drake_file = open("/Users/davidrusso/Documents/Classes/Python Certificate/Advanced Python/Sp2018-Online/students/david_russo/lesson02/drake_songs.txt", 'w')
for track in drake_tracks:
    drake_file.write(str(track) + "\n")
drake_file.close()