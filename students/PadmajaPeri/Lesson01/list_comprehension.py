import pandas as pd

"""
Method that computes the most danceable tracks
"""
def most_danceable_tracks(file_name):
    music = pd.read_csv(file_name)
    return [(artists, name) for danceability, loudness, artists, name in zip(sorted(music.danceability), music.loudness,
                                                                             music.artists, music.name)
            if danceability > 0.8 and loudness < -5.0]


if __name__ == '__main__':
    print(most_danceable_tracks('featuresdf.csv'))
