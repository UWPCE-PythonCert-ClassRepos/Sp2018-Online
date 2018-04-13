import pandas as pd


def fav_tracks_generator():
    music = pd.read_csv("featuresdf.csv")
    zipped_data = zip(music.artists, music.name)
    filtered_list = [song for song in zipped_data if song[0] == 'Ed Sheeran']
    while True:
        yield filtered_list.pop()


def test_generator():

    g = fav_tracks_generator()

    assert next(g) == ('Ed Sheeran', 'Perfect')
    assert next(g) == ('Ed Sheeran', 'Galway Girl')
    assert next(g) == ('Ed Sheeran', 'Castle on the Hill')
    assert next(g) == ('Ed Sheeran', 'Shape of You')

if __name__ == '__main__':
    test_generator()