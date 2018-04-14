#!/usr/bin/env python3

'''
Name:       homework01.py
Author:     Eric Rosko
Date:       Apr 8, 2018
Python ver. 3.4.3
'''

import pandas as pd
import pprint
from collections import namedtuple


def hello():
    return "hello"


music = pd.read_csv("featuresdf.csv")
#  pandas.core.frame.DataFrame
# print(type(music.info))

# df = DataFrame(randn(8, 4), columns=['A', 'B', 'C', 'D'])
df = music


def iternamedtuples(df):
    Row = namedtuple('Song', df.columns)
    for row in df.itertuples():
        yield Row(*row[1:])


'''
('Migos', 'Bad and Boujee (feat. Lil Uzi Vert)')
('Drake', 'Fake Love')
('Kendrick Lamar', 'HUMBLE.')
('21 Savage', 'Bank Account')
('Jax Jones', "You Don't Know Me - Radio Edit")
('Liam Payne', 'Strip That Down')
('Future', 'Mask Off')
('Zion & Lennox', 'Otra Vez (feat. J Balvin)')
('Drake', 'Passionfruit')
'''
def filterByDanceabilityAndLoudness():
    music = pd.read_csv("featuresdf.csv")
    named_tuples = iternamedtuples(df)
    both = filter(lambda x: x.danceability > 0.8 and x.loudness < -5.0, named_tuples)
    sortedItems = sorted(tuple(both), key=lambda x: x.danceability, reverse = True)

    myList = list()
    for i in sortedItems:
        temp = (i.artists, i.name)
        myList.append(temp)
    return myList

# it = iternamedtuples(df)
# # print("len is ", len(list(filter(lambda x: x.danceability > 0.8, list(it)))


# # <generator object iternamedtuples at 0x1057a0360>
# # print(iternamedtuples(df))

# filter_list = list(filter(lambda x: x.key == 1.0, df_list))
# # print(df_list)


# #Row(id='7qiZfU4dY1lWllzX7mPBI'..., time_signature=4.0)
# x = filter(lambda x: x.danceability > 0.8, df_list)
# danceab = list(filter(lambda x: x.danceability > 0.8, df_list))
# loud = list(filter(lambda x: x.loudness < -5.0, df_list))
# both = list(filter(lambda x: x.danceability > 0.8 and x.loudness < -5.0, df_list))
# # for item in list(x):
# #     print(item)

# print("len of df_list", len(df_list))
# print("len of filter_list", len(filter_list))
# print("len of danceab", len(danceab))
# print("len of both", len(both))
# print("len of loud", len(loud))

# print(list(x))
# for x in df_list:
#     print(x)
