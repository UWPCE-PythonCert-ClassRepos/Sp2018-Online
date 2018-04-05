#!/usr/bin/env python3
"""Solutions to Lesson01 comprehensions assignment re music."""
import pandas as pd
# import time

# Instructions summary:
# 1) get artists and song names for tracks with danceability scores over 0.8
# and loudness scores below -5.0.
# 2) these tracks should be sorted in descending order by danceability
# 3) top five tracks are selected and printed

# Load the database
music = pd.read_csv("featuresdf.csv")

# Three versions of solution -- all results are identical

# INITIAL SOLUTION -- with indixing
# start_time1 = time.time()
res1 = sorted(
              [
               (music.name[i],
                music.artists[i],
                round(music.danceability[i], 2),
                round(music.loudness[i], 2))
               for i in range(len(music))
               if music.danceability[i] > 0.8 and music.loudness[i] < -5.0
               ],
              key=lambda x: x[2],
              reverse=True
              )[0:5]
# mytime1 = time.time() - start_time1
# print("Elapsed time = ", mytime1)
print(res1)
# prints
# [('Bad and Boujee (feat. Lil Uzi Vert)', 'Migos', 0.93, -5.31),
#  ('Fake Love', 'Drake', 0.93, -9.43),
#  ('HUMBLE.', 'Kendrick Lamar', 0.9, -6.84),
#  ("You Don't Know Me - Radio Edit", 'Jax Jones', 0.88, -6.05),
#  ('Bank Account', '21 Savage', 0.88, -8.23)]


# SECOND SOLUTION -- with list comprehension and zip - THIS MUST BE IT
# n, a, d, l are for name, artist, danceability, and loudness
# start_time2 = time.time()
res2 = sorted(
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
# mytime2 = time.time() - start_time2
# print("Elapsed time = ", mytime2)
print(res2)
# prints
# [('Bad and Boujee (feat. Lil Uzi Vert)', 'Migos', 0.93, -5.31),
#  ('Fake Love', 'Drake', 0.93, -9.43),
#  ('HUMBLE.', 'Kendrick Lamar', 0.9, -6.84),
#  ("You Don't Know Me - Radio Edit", 'Jax Jones', 0.88, -6.05),
#  ('Bank Account', '21 Savage', 0.88, -8.23)]


# Solution No. 3 -- with generator expression instead of list comprehension
# n, a, d, l are for name, artist, danceability, and loudness
# Not sure if this solution is any better, if I measure the time correctly.
# start_time3 = time.time()
res3 = sorted(
              (
               (n, a, round(d, 2), round(l, 2))
               for n, a, d, l in zip(music.name,
                                     music.artists,
                                     music.danceability,
                                     music.loudness
                                     )
               if d > 0.8 and l < -5.0
               ),
              key=lambda x: x[2],
              reverse=True
              )[0:5]
# mytime3 = time.time() - start_time3
# print("Elapsed time = ", mytime3)
print(res3)
# prints
# [('Bad and Boujee (feat. Lil Uzi Vert)', 'Migos', 0.93, -5.31),
#  ('Fake Love', 'Drake', 0.93, -9.43),
#  ('HUMBLE.', 'Kendrick Lamar', 0.9, -6.84),
#  ("You Don't Know Me - Radio Edit", 'Jax Jones', 0.88, -6.05),
#  ('Bank Account', '21 Savage', 0.88, -8.23)]
