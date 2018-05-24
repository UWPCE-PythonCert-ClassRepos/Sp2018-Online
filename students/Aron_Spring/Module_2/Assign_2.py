import os
import csv
import pandas as pd

with open('featuresdf.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

def fav_artist():
    with open('featuresdf.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            artist = str(line[2])
            name = line[1]
            if artist == "Ed Sheeran":
                yield(name)

def energetic_track_finder(min_energy_level=0.8):
    music = pd.read_csv("featuresdf.csv")
    def get_tracks():
        music, min_energy_level
        zipped_data = zip(music.artists, music.name, music.energy)
        filtered_list = [song for song in zipped_data if song[2] > min_energy_level]
        return filtered_list
    return get_tracks

import csv
# def fav_artist(n = "Ed Sheeran"):
#     with open('featuresdf.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for line in csv_reader:
#             artist = str(line[2])
#             name = line[1]
#             if artist == n:
#                 music_list2.append((name, artist))
#         def find_music():
#             return music_list2
#         return find_music