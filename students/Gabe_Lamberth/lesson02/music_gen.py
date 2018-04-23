#!/usr/bin/env python3

import pandas as pd
from pprint import pprint
from pathlib import Path


def main():
    """
        Using pathlib library to read in file assuming file and program store in same location
        """
    cwd = Path.cwd()

    pth = cwd / 'featuresdf.csv'

    # Load data
    df = pd.read_csv("featuresdf.csv")

    zip_df = zip(df.artists, df.name)

    print("-----Part 1-----")
    # Part 1 -- Generators
    print(''.join([f'{artist}, {name}\n' for artist, name in zip_df if artist == 'Ed Sheeran']), end=' ')

    # Part 2 -- closure
    def music_function(df):
    
        def get_music(level):
            return ''.join([f'{artist}, {name}, {energy:.1f}\n' for artist, name, energy in df if energy > level])

        return get_music


    print("\n-----Part 2-----")

    dataset = zip(df.artists, df.name, df.energy)

    music_level = music_function(dataset)
    print(music_level(0.8))


if __name__ == "__main__":
    main()
