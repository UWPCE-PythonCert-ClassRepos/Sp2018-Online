#!/usr/bin/env python3
import pandas as pd


def favorite_artist_tracks_generator(artist):
    """
    Generator that generates tracks of an artist passed in as a parameter
    :param string. Artist name
    :return: string. Track name
    """
    music = pd.read_csv('featuresdf.csv')
    for index, row in music.iterrows():
        if row['artists'] == artist:
            yield row['name']


def favorite_artist_tracks_gen_exp(favorite_artist):
    """ Generator expression that returns the tracks of an artist passed as a parameter """
    music = pd.read_csv('featuresdf.csv')
    return ((artists, name) for danceability, loudness, artists, name in zip(sorted(music.danceability), music.loudness,
                                                                             music.artists, music.name)
            if artists == favorite_artist)


def high_energy_tracks(favorite_artist):
    """ Closure that is used to get the high energy tracks of an artist passed as a parameter """
    music = pd.read_csv('featuresdf.csv')

    def favorite_artist_high_energy_tracks():
        return [(artists, name, energy) for artists, name, energy in zip(music.artists, music.name, music.energy)
                if artists == favorite_artist and energy > 0.8]
    return favorite_artist_high_energy_tracks()


if __name__ == '__main__':
    """ Test for generator that generates favorite_artist_tracks """
    a_gen = favorite_artist_tracks_generator('Ed Sheeran')
    while True:
        try:
            track = next(a_gen)
        except StopIteration:
            break
        else:
            print("Track is:{}".format(track))

    """ Test for Generator Expression that generates favorite_artist tracks """
    b_gen = favorite_artist_tracks_gen_exp('Luis Fonsi')
    while True:
        try:
            track = next(b_gen)
        except StopIteration:
            break
        else:
            print("Track is:{}".format(track))

    """ Test for printing high energy tracks of an artist """
    print(high_energy_tracks('Ed Sheeran'))