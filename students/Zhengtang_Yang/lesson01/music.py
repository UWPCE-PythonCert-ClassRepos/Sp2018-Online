import pandas as pd
music = pd.read_csv("featuresdf.csv")
# print(music.head())
# print(music.describe())
res = music[[x > 0.8 and y < -5.0 for x, y in zip(music.danceability, music.loudness)]]
sorted_res = res.sort_values(by = ['danceability'], ascending = False)
top5_res = sorted_res.head(5)
print(top5_res[:])