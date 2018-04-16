# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:43:32 2018

@author: seelc
"""

import pandas as pd
import numpy as np

music = pd.read_csv("featuresdf.csv")
music.head()
music.describe()

categories = list(music.columns.values)


new_list = [x for x in music.danceability if x > 0.8]

danceable_songs = pd.DataFrame(columns = categories)
for i in new_list:
    for y in range(len(music.danceability)):
        
        if music.loc[y, "danceability"] == i:
            song = music.loc[y,:]
            danceable_songs = danceable_songs.append(song)
            
#Generator that returns pritns Ed Sheeran soundtracks from the 2017 top 100 list            
def return_fav():
    count_row = 0
    while count_row < len(music.loc[:, "artists"]):
        current = str(music.loc[count_row, "artists"])
        if current == "Ed Sheeran":
            print(music.loc[count_row, :])
            yield music.loc[count_row, :]
        count_row = count_row + 1


#a = return_fav()
#next(a)

#Returns all songs with an "energy" > 8.0 storred in the 2017 top 100
def outside(songs):
    
    def inside():
        song_list = list() 
        row_count = 0.0
        while row_count < len(songs):
            if songs.loc[row_count, "energy"] > 0.8:
                print(songs.loc[row_count, :])
                song_list.append(songs.loc[row_count, :])    
            row_count = row_count + 1
            
        return song_list
    return inside()
    
b = outside(music)
        
