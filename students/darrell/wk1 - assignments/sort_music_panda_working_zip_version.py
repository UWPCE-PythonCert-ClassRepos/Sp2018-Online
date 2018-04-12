import pandas as pd

music = pd.read_csv("featuresdf.csv")

# zip all the data
zipped_data = zip(music.artists,music.name,music.danceability,music.loudness)

# comprehension with conditionals, sorted by 3rd column i.e. danceability, reverse sorted
sorted_list = sorted([song for song in zipped_data if song[2] >0.8 and song[3]< -5.0],key=lambda song_col: song_col[2], reverse=True)

[print(song) for song in sorted_list]

