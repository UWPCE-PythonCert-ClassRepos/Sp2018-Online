#!/usr/bin/env python3
#
# 1. "Fake Love" by Drake (tie, quieter song)
# 2. "Bad and Boujee (feat. Lil Uzi Vert)" by Migos
# 3. "HUMBLE." by Kendrick Lamar
# 4. "Bank Account" by 21 Savage
# 5. "You Don't Know Me - Radio Edit" by Jax Jones

import pandas as pd

music = pd.read_csv("featuresdf.csv")

base_export = zip(music.name, music.artists, music.danceability, music.loudness)
filter1 = [(w, x, y, z) for (w, x, y, z) in base_export if y > 0.8]
filter2 = [(w, x, y, z) for (w, x, y, z) in filter1 if z < -5.0]
solution = sorted(filter2, key=lambda filter2: filter2[2], reverse=True)
print(solution)