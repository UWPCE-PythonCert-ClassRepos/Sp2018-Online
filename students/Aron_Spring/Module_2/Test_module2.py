"""
testing of module 2 - Assign_2.py

"""

import Assign_2 as mod_two

#Test of energentic function - track count
dancelist = mod_two.energetic_track_finder()
assert len(dancelist()) == 19
assert dancelist()[-1] == ('The Chainsmokers', "Don't Let Me Down", 0.8590000000000001)

#Test of fav artist function - track count

def test_fav_artist():

    g = mod_two.fav_artist()

    assert next(g) == 'Shape of You'
    assert next(g) == 'Castle on the Hill'



