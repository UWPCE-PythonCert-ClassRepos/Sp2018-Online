#!/usr/bin/env python
'''sorted music assignment for lesson 1
I used pandas, but played around for a while with creating a tuple from the csv and manipulating it too.
'''

def sort_by_danceability_and_loudness(dance_min = 0.8, loudness_max = -5.0,csv_in = 'c:\\test\\featuresdf.csv'):
    import pandas as pd
    music = pd.read_csv(csv_in)
    music_zip = zip(music.artists,music.name,music.danceability,music.loudness)
    music_list = sorted([track for track in music_zip if track[2] >0.8 and track[3]< -5.0],key=lambda track_name: track_name[1])
    return music_list

if __name__ == '__main__':

    my_music = sort_by_danceability_and_loudness()
    print(my_music)
