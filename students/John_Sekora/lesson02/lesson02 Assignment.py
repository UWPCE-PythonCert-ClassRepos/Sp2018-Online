# John Sekora
# Class 2, Lesson02, Generators & Closures
# UW Certificate in Python, 4/15/2018

# ######################################################################################
# GENERATORS
# Last week we looked at Spotify’s top tracks from 2017.
# We used comprehensions and perhaps a lambda to find tracks we might like.
# Having recovered from last week’s adventure in pop music we’re ready to venture back.
# Write a generator to find and print all of your favorite artist’s tracks from the data set.
# Your favorite artist isn’t represented in that set? In that case, find Ed Sheeran’s tracks.
# Load the data set following the instructions from last week.
# Submit your generator expression and the titles of Ed’s tracks.

# CLOSURES
# Using the same data set, write a closure to capture high energy tracks.
# We will define high energy tracks as anything over 8.0.
# Submit your code and the tracks it finds, artist name, track name and energy value.
# ######################################################################################


import pandas as pd

# Load the data
music = pd.read_csv("featuresdf.csv")

# GENERATOR
generator = (x for x, y in zip(music.name, music.artists) if y == "Ed Sheeran")
print(list(generator))


# CLOSURE (List Comprehension)
def outer(data):

    def inner():
        lst_comp = [(x, y, cond) for x, y, cond in zip(data.artists, data.name, data.energy) if cond > 0.8]
        print(lst_comp)

    return inner


high_energy_closure = outer(music)
high_energy_closure()

