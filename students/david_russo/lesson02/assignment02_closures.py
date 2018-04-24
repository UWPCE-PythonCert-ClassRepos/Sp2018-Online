#!/usr/bin/env python

import pandas as pd
import operator

# read music in as pandas data frame
music = pd.read_csv("/Users/davidrusso/Documents/Classes/Python Certificate/Advanced Python/Sp2018-Online/students/david_russo/lesson02/featuresdf.csv", encoding = "ISO-8859-1")

# Write a closure to capture tracks whose 'energy' is over 0.80
def find_high_energy_tracks(energy_threshold):

	# create function to get tracks higher than a specified energy
    def filter_energy(x):
        if x > energy_threshold:
            return True
        else:
            return False
	        
    # return filter_energy function
    return filter_energy
    

energy_80 = find_high_energy_tracks(0.80)

def get_high_energy_song_attributes():
    song_index = 0
    while song_index < len(music):
        if energy_80(music['energy'][song_index]):
            yield song_index
        song_index += 1

energy_tracks_over_80 = get_high_energy_song_attributes()

# write the high energy tracks to file
high_energy_songs = open("/Users/davidrusso/Documents/Classes/Python Certificate/Advanced Python/Sp2018-Online/students/david_russo/lesson02/high_energy_songs.txt", 'wb')
for idx in energy_tracks_over_80:
    high_energy_songs.write(u'\t'.join((music['artists'][idx], music['name'][idx], str(music['energy'][idx]), '\n')).encode('utf-8'))
high_energy_songs.close()

    

