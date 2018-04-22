#!/usr/bin/env python3
#
# Spotify Generator
# Chay Casso, 4/15/18
#
# Ed Sheeran songs:
# "Shape of You"
# "Castle on the Hill"
# "Galway Girl"
# "Perfect"


import pandas as pd

music = pd.read_csv("featuresdf.csv")
ed_songs = filter((lambda x: x[1] == "Ed Sheeran"), zip(music.name, music.artists))
solution = list(ed_songs)
print(solution)