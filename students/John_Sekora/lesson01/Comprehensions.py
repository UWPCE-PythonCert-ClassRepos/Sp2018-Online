# John Sekora
# Class 2, Lesson01, Comprehensions
# UW Certificate in Python, 4/8/2018

import pandas as pd

# Load the data
music = pd.read_csv("featuresdf.csv")

# View the top 5 rows of every variable
print("\n Heading of Music \n")
print(music.head())

# View a statistical description for each variable
print("\n Statistical Description for Each Variable \n")
print(music.describe())


'''
We want music we can dance to (danceability > 0.8), that isn't too loud (loudness < -5.0)
Sort the data by descending order of danceability, and display the Top 5 Songs
The following functions may be helpful:   zip() and sorted()
'''

# zip() is a really cool functional programming tool from pandas that takes multiple lists and restructures
# them together into what I can see as a "zip object".
# Searching the directory for zip, I see a special method, __next__, which tells me the output is an iterator
zipped = zip(music.artists, music.name, music.danceability, music.loudness)


# sorted() is another functional programming tool from pandas
# It allows conditions to be placed on the data for filtering purposes, then sort through the use of a lambda function
sorted_list = sorted([song for song in zipped if song[2] > 0.8 and song[3] < -5.0],
                     key=lambda sort_element: sort_element[2], reverse=True)


# this is a list comprehension to list the Top 5 songs for preference in music
print("\n Top 5 Songs \n")
[print(song) for song in sorted_list[0:5]]





