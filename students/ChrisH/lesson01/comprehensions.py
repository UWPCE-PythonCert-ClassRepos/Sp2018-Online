#!/usr/bin/env python3
# -----------------------------------------------------------
# comprehensions.py
#   Uses a comprehension to get artists and song names for
#   tracks with danceability scores over 0.8 and loudness scores below -5.0
#   Using the Spotify top 100 list for 2017 from a csv file
# -----------------------------------------------------------

import pandas as pd


if __name__ == "__main__":

    music = pd.read_csv('featuresdf.csv')

    print('sorted pre list comprehension')
    tl = [t for t in
          sorted(zip(music.artists, music.name, music.loudness, music.danceability),
                 key=lambda t: t[3], reverse=True)
          if t[2] < -0.5 and t[3] > 0.8]

    for i in tl[:5]:
        print(f'"{i[1]}" by {i[0]}')

    print('\nsorted post comprehension')
    t2 = sorted([t for t in
                 zip(music.artists, music.name, music.loudness, music.danceability)
                 if t[2] < -0.5 and t[3] > 0.8],
                key=lambda t: t[3], reverse=True)

    for i in t2[:5]:
        print(f'"{i[1]}" by {i[0]}')
