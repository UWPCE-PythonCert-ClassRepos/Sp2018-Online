import pandas as pd

# Task 1
# Write a generator to find and print all of your favorite artist’s tracks from the data set. Your favorite artist isn’t
# represented in that set? In that case, find Ed Sheeran’s tracks.

# Task 2
# Using the same data set, write a closure to capture high energy tracks. We will define high energy tracks as anything over 8.0.
# Submit your code and the tracks it finds, artist name, track name and energy value.
music = pd.read_csv('featuresdf.csv')

def generator_expression_for_favorite_tracks():
    """
    Generator expression to retrieve favorite music tracks.
    :return:
    """
    return (name for name, artist in zip(music.name, music.artists) if artist == "Ed Sheeran")


def closure_for_high_energy_tracks(data):
    """
    closure function for retrieving high energy track nmaes, artist names with energy levels.
    :param data:  Music data read from csv file
    """
    def high_energy_return_function(energy_level):
        return [(artist, name, energy) for artist, name, energy in zip(data.artists, data.name, data.energy)
                if energy > energy_level]

    return high_energy_return_function


# High energy tracks with energy level > 0.8
music_energy  = closure_for_high_energy_tracks(music)
print(music_energy(0.8))
# [('Luis Fonsi', 'Despacito - Remix', 0.815), ('Post Malone', 'Congratulations', 0.812),
#  ('Jason Derulo', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 0.8170000000000001),
# ('Ed Sheeran', 'Castle on the Hill', 0.8340000000000001), ('Imagine Dragons', 'Thunder', 0.81),
# ('Danny Ocean', 'Me Rehúso', 0.804), ('Ed Sheeran', 'Galway Girl', 0.8759999999999999),
# ('The Weeknd', 'I Feel It Coming', 0.813), ('Starley', 'Call On Me - Ryan Riback Extended Remix', 0.843),
# ('Martin Jensen', 'Solo Dance', 0.836), ('Enrique Iglesias', 'SUBEME LA RADIO', 0.823), ('Maggie Lindemann', 'Pretty Girl - Cheat Codes X CADE Remix', 0.868), ('Bruno Mars', '24K Magic', 0.8029999999999999), ('Katy Perry', 'Chained To The Rhythm', 0.8009999999999999), ('Wisin', 'Escápate Conmigo', 0.8640000000000001), ('Steve Aoki', 'Just Hold On', 0.932), ('CNCO', 'Reggaetón Lento (Bailemos)', 0.838), ('The Vamps', 'All Night', 0.809), ('The Chainsmokers', "Don't Let Me Down", 0.8590000000000001)]


