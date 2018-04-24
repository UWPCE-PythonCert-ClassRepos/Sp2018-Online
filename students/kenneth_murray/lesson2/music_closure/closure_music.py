#!/usr/bin/env python
"""
Lesson2 Create a closure for high energy music list of songs
"""


def music_energy_factory(energy, csv_in='c:\\test\\featuresdf.csv'):
    import pandas as pd
    music = pd.read_csv(csv_in)
    music_zip = zip(music.artists, music.name, music.energy)
    def music_energy():
        nonlocal energy
        nonlocal music_zip
        return sorted([track for track in music_zip if track[2] > energy], key=lambda track_energy: track_energy[1])
    return music_energy()


if __name__ == '__main__':
    from pprint import pprint

    he_music = music_energy_factory(energy=.8)
    pprint(he_music)
