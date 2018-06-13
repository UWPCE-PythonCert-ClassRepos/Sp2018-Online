#!/usr/bin/env python3

'''
Author: Eric Rosko
Date:   June 12, 2018
File:   news_downloader.py
Usage:

'''

from threading import Thread
import queue
import time
import requests
import json

newsapi_key = "xxxx" # api key goes here

url = "https://newsapi.org/v2/top-headlines?" \
"country=us&apiKey={0}".format(newsapi_key)
r = requests.get(url)

temp_json = r.json()

for a in temp_json['articles']:
    print(a)
    break

# print(temp_json['articles'])


if __name__ == "__main__":
    pass
