import pandas as pd
import numpy as np

music = pd.read_csv("featuresdf.csv")


def favorite(artist):
    for track in music.name.loc[music['artists'] == artist]:
        yield track

generate_favorite_tracks = favorite('Ed Sheeran')

next(generate_favorite_tracks)
next(generate_favorite_tracks)
next(generate_favorite_tracks)
next(generate_favorite_tracks)

#Results:
#'Shape of You'
#'Castle on the Hill'
#'Galway Girl'
#'Perfect'

#Closure
#Using the same data set, write a closure to capture high energy tracks. We will define high energy tracks as anything over 8.0. 
def high_energy(dataset):
    def high_energy_only():
        high_energy_subset = dataset[dataset['energy'] > 0.8]
        return high_energy_subset[['name', 'artists', 'energy']]
    return high_energy_only()

energy_tracks = high_energy(music)

print(energy_tracks)

#Results
#                                          name           artists  energy
#                            Despacito - Remix        Luis Fonsi   0.815
#                             Congratulations       Post Malone   0.812
#  Swalla (feat. Nicki Minaj & Ty Dolla $ign)      Jason Derulo   0.817
#                          Castle on the Hill        Ed Sheeran   0.834
#                                     Thunder   Imagine Dragons   0.810
#                                   Me Rehúso       Danny Ocean   0.804
#                                 Galway Girl        Ed Sheeran   0.876
#                            I Feel It Coming        The Weeknd   0.813
#     Call On Me - Ryan Riback Extended Remix           Starley   0.843
#                                  Solo Dance     Martin Jensen   0.836
#                             SUBEME LA RADIO  Enrique Iglesias   0.823
#      Pretty Girl - Cheat Codes X CADE Remix  Maggie Lindemann   0.868
#                                   24K Magic        Bruno Mars   0.803
#                       Chained To The Rhythm        Katy Perry   0.801
#                            Escápate Conmigo             Wisin   0.864
#                                Just Hold On        Steve Aoki   0.932
#                  Reggaetón Lento (Bailemos)              CNCO   0.838
#                                   All Night         The Vamps   0.809
#                           Don't Let Me Down  The Chainsmokers   0.859


