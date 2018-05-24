import pandas as pd


def fav_artist_generator(fav_artist):
    """ Generator to generate tracks of a favorite artist """
    music = pd.read_csv('featuresdf.csv')
    for index, row in music.iterrows():
        if row['artists'] == fav_artist:
            yield row['name']


def fav_artist_tracks_generator(fav_artist):
    """ Generator expression that returns the tracks of a favorite artist """
    music = pd.read_csv('featuresdf.csv')
    return ((artists, name) for danceability, loudness, artists, name in zip(sorted(music.danceability), music.loudness,
                                                                             music.artists, music.name)
            if artists == fav_artist)



def high_energy_track(fav_artist):
    """ Closure to get the high energy tracks of favorite artist """
    music = pd.read_csv('featuresdf.csv')
    return [(artists, name, energy) for artists, name, energy in zip(music.artists, music.name, music.energy)
                if artists == fav_artist and energy > 0.8]


if __name__ == '__main__':

    first_gen = fav_artist_generator('Ed Sheeran')
    while True:
        try:
            fav_track = next(first_gen)
        except StopIteration:
            break
        else:
            print("The track of favorite artist {} is :{}".format('Ed Sheeran', fav_track))

    second_gen = fav_artist_tracks_generator('Bruno Mars')
    while True:
        try:
            track = next(second_gen)
        except StopIteration:
            break
        else:
            print("The track is: {} for {}".format(track[1], 'Bruno Mars'))

    h_energy = high_energy_track('Ed Sheeran')
    for i in range(len(h_energy)):
        print("The high energy track of {} is {} with energy {}".format(h_energy[i][0], h_energy[i][1], h_energy[i][2]))
