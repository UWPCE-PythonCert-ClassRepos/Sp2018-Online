#!/usr/bin/env python3

"""Lesson02 - generators / closures - music tracks."""

import pandas as pd

# Assignment summary:
# 1) Write a generator to find and print all of Ed Sheeran’s tracks
#  from the data set. Submit your generator expression and the titles of
#  Ed’s tracks.
#
# 2) Write a closure to capture high energy tracks - anything over 8.0
#  Submit your code and the tracks it finds: artist name, track name and
#  energy value.

# Load data
music = pd.read_csv("featuresdf.csv")

# PART 1 -- generator expression
res = (name for name, artist in zip(music.name, music.artists)
       if artist == "Ed Sheeran")

print(list(res))
#  prints
# ['Shape of You', 'Castle on the Hill', 'Galway Girl', 'Perfect']


# PART 2 -- closure
def energy_music_factory(dataset):
    """A closure to create energy_music_function.

    Arg: dataset: a pandas dataset from .scv-file to close into the
    returned function.
    """
    def energy_music_function(energy_level):
        return [(artist, name, energy)
                for artist, name, energy in zip(dataset.artists,
                                                dataset.name,
                                                dataset.energy)
                if energy > energy_level]

    return energy_music_function


energy_music = energy_music_factory(music)
print(energy_music(0.8))
# [('Luis Fonsi', 'Despacito - Remix', 0.815), ('Post Malone', 'Congratulations',
# 0.812), ('Jason Derulo', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 0.8170000
# 000000001), ('Ed Sheeran', 'Castle on the Hill', 0.8340000000000001), ('Imagine
# Dragons', 'Thunder', 0.81), ('Danny Ocean', 'Me Rehúso', 0.804), ('Ed Sheeran',
# 'Galway Girl', 0.8759999999999999), ('The Weeknd', 'I Feel It Coming', 0.813), (
# 'Starley', 'Call On Me - Ryan Riback Extended Remix', 0.843), ('Martin Jensen',
# 'Solo Dance', 0.836), ('Enrique Iglesias', 'SUBEME LA RADIO', 0.823), ('Maggie L
# indemann', 'Pretty Girl - Cheat Codes X CADE Remix', 0.868), ('Bruno Mars', '24K
#  Magic', 0.8029999999999999), ('Katy Perry', 'Chained To The Rhythm', 0.80099999
# 99999999), ('Wisin', 'Escápate Conmigo', 0.8640000000000001), ('Steve Aoki', 'Ju
# st Hold On', 0.932), ('CNCO', 'Reggaetón Lento (Bailemos)', 0.838), ('The Vamps'
# , 'All Night', 0.809), ('The Chainsmokers', "Don't Let Me Down", 0.8590000000000
# 001)]


# Testing the closure
res2 = [(a, n, e) for a, n, e in zip(music.artists,
                                     music.name,
                                     music.energy)
        if e > 0.8]
assert energy_music(0.8) == res2


# My thought process when writing the closure -- to be deleted later
# class MyMusic:
#     def __init__(self, dataset):
#         self.dataset = dataset
#
#     def energy(self, level):
#         return [(a, n, e) for a, n, e in zip(music.artists,
#                                              music.name,
#                                              music.energy)
#                 if e > level]
#
# all_music = MyMusic(music)
# highenergy = all_music.energy(0.8)
# assert highenergy == res2
