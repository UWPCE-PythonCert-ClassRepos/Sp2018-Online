#!/usr/bin/env python3

'''
Name:       test_homework02.py
Author:     Eric Rosko
Date:       Apr 15, 2018
Python ver. 3.6.5

Usage:  py.test -sv ./test_homework02.py
'''


from homework02 import *
from pprint import pprint
import collections

def test_generate_favorite_artist_ed_sheeran():
    result = favorite_artist()
    # pprint(result)
    assert len(result) == 4

    expected = [('Ed Sheeran', 'Castle on the Hill'),
                ('Ed Sheeran', 'Galway Girl'),
                ('Ed Sheeran', 'Perfect'),
                ('Ed Sheeran', 'Shape of You')]

    assert sorted(result, key = lambda a: a) == expected


def test_get_energy_tracks_above_08_with_closure():
    assert len(g_songs) == 0
    filter_with_closure()

    assert len(g_songs) == 19

    expected = [('24K Magic', 'Bruno Mars', 0.8029999999999999),
    ('All Night', 'The Vamps', 0.809),
    ('Call On Me - Ryan Riback Extended Remix', 'Starley', 0.843),
    ('Castle on the Hill', 'Ed Sheeran', 0.8340000000000001),
    ('Chained To The Rhythm', 'Katy Perry', 0.8009999999999999),
     ('Congratulations', 'Post Malone', 0.812),
     ('Despacito - Remix', 'Luis Fonsi', 0.815),
     ("Don't Let Me Down", 'The Chainsmokers', 0.8590000000000001),
     ('Escápate Conmigo', 'Wisin', 0.8640000000000001),
     ('Galway Girl', 'Ed Sheeran', 0.8759999999999999),
     ('I Feel It Coming', 'The Weeknd', 0.813),
      ('Just Hold On', 'Steve Aoki', 0.932),
      ('Me Rehúso', 'Danny Ocean', 0.804),
      ('Pretty Girl - Cheat Codes X CADE Remix', 'Maggie Lindemann', 0.868),
      ('Reggaetón Lento (Bailemos)', 'CNCO', 0.838),
       ('SUBEME LA RADIO', 'Enrique Iglesias', 0.823),
        ('Solo Dance', 'Martin Jensen', 0.836),
         ('Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 'Jason Derulo', 0.8170000000000001),
          ('Thunder', 'Imagine Dragons', 0.81)]
    assert g_songs == expected


if __name__ == "__main__":
    test_generate_favorite_artist_ed_sheeran()
    test_get_energy_tracks_above_08_with_closure()
