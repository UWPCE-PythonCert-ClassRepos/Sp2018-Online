#!/usr/bin/env python3
"""Solutions to Lesson01 comprehensions assignment re music."""
import pandas as pd

# Instructions summary:
# 1) get artists and song names for tracks with danceability scores over 0.8
# and loudness scores below -5.0.
# 2) these tracks should be sorted in descending order by danceability
# 3) top five tracks are selected and printed

# Load the database
music = pd.read_csv("featuresdf.csv")


# n, a, d, l are for name, artist, danceability, and loudness
res = sorted(
              [
               (n, a, round(d, 2), round(l, 2))
               for n, a, d, l in zip(music.name,
                                     music.artists,
                                     music.danceability,
                                     music.loudness
                                     )
               if d > 0.8 and l < -5.0
               ],
              key=lambda x: x[2],
              reverse=True
              )[0:5]

print(res)
# prints
# [('Bad and Boujee (feat. Lil Uzi Vert)', 'Migos', 0.93, -5.31),
#  ('Fake Love', 'Drake', 0.93, -9.43),
#  ('HUMBLE.', 'Kendrick Lamar', 0.9, -6.84),
#  ("You Don't Know Me - Radio Edit", 'Jax Jones', 0.88, -6.05),
#  ('Bank Account', '21 Savage', 0.88, -8.23)]
