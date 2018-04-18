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

    # Dump file path into pandas data frame
    df = pd.read_csv(pth)
    """
    This compression took sometime to figure out. Thanks for the "zip" tip
    After researching what pandas did to csv files by way of creating a data frame,
    I figured out that each column could be...well zipped together and create a quasi database 
    """
    # pprint([f'{a}, {b}, {c:.2f}, {d:.2f}' for a, b, c, d in zip(df.artists, df.name, df.danceability, df.loudness)
    #        if c > 0.8 and d < -5.0])

    # for code read ability, I assign the data frames to one variable and dumped the pprint feature
    zip_df = zip(df.artists, df.name, df.danceability, df.loudness)

    print(''.join([f'{a}, {b}, {c:.2f}, {d:.2f}\n' for a,b,c,d in zip_df if c > 0.8 and d < -5.0]), end=' ')


if __name__ == "__main__":
    main()