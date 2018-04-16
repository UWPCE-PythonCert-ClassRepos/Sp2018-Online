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
            

correct_loudness = danceable_songs.ix[danceable_songs['loudness'] < -5.0]
correct_loudness.sort_values(by = "danceability", ascending = True)

