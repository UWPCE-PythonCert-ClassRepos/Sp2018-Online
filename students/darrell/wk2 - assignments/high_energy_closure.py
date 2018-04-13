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


def energetic_track_finder(min_energy_level=0.8):
    music = pd.read_csv("featuresdf.csv")
    def get_tracks():
        nonlocal music, min_energy_level
        zipped_data = zip(music.artists, music.name, music.energy)
        filtered_list = [song for song in zipped_data if song[2] > min_energy_level]
        return filtered_list
    return get_tracks

def test_energetic_track_finder():
    high_energy = energetic_track_finder(0.8)
    med_to_high = energetic_track_finder(0.5)
    off_the_charts = energetic_track_finder(10)

    assert len(high_energy()) == 19
    assert len(med_to_high()) == 84
    assert len(off_the_charts()) == 0


if __name__ == '__main__':
    test_generator()
    test_energetic_track_finder()