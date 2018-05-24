import pandas as pd

music = pd.read_csv("featuresdf.csv")

# Get artists and song names for tracks with danceability
# scores over 0.8 and loudness scores below -5.0
just_right = music.loc[(music['danceability'] > 0.8) & (music['loudness'] < -5.0)]

# Sort Tracks in descending order by danceability
sorted_just_right = just_right.sort_values('danceability', ascending=False)

# Submit code along with top five tracks
print(sorted_just_right[['artists','name']][0:5])

# Prints
#            artists                                 name
# 48           Migos  Bad and Boujee (feat. Lil Uzi Vert)
# 51           Drake                            Fake Love
# 5   Kendrick Lamar                              HUMBLE.
# 94       21 Savage                         Bank Account
# 62       Jax Jones       You Don't Know Me - Radio Edit
