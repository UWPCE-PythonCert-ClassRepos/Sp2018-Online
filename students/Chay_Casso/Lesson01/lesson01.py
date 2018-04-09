#!/usr/bin/env python3
#

import pandas as pd

music = pd.read_csv("featuresdf.csv")

base_export = zip(music.name, music.danceability, music.loudness)
filter1 = [(x, y, z) for (x, y, z) in base_export if y > 0.8]
filter2 = [(x, y, z) for (x, y, z) in filter1 if z < -5.0]
solution = sorted(filter2, key=lambda filter2: filter2[1], reverse=True)
print(solution)