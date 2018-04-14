#!/usr/bin/env python

import pandas as pd
import operator

# read music in as pandas data frame
music = pd.read_csv("/Users/davidrusso/Documents/Classes/Python Certificate/Advanced Python/Sp2018-Online/students/david_russo/lesson01/featuresdf.csv", encoding = "ISO-8859-1")

music.head()
music.describe()

# get songs with a danceability score greater than 0.8
[x for x in music.danceability if x > 0.8]

# get songs with a danceability score greater than 0.8 with a loudness less than -5.0
top_5_results = music[[x > 0.8 and y < -5.0 for x, y in zip(music.danceability, music.loudness)]].sort_values(by = ['danceability'], ascending = False).name.head(5)

top_5_results.to_csv('top_five_results.txt', header = True, index = False)






