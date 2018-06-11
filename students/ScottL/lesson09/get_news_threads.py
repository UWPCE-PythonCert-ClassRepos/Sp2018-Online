#!/usr/bin/env python

# -------------------------------------------------#
# Title: get_news_threads.py
# Dev: Scott Luse
# Date: 06/10/2018
# Assignment: Get the news sources from newsapi.org
# and determine how many times a keyword is used in
# in article titles; use multiple threads
#
# Logic Flow:
# Step-1: get source list from newsapi same as before
# Step-2: split source list in half for two threads
# Step-3: start threads using target and source lists
# Step-4: worker function updates global title list
# Step-5: main thread waits for worker threads
# Step-6: count key WORD after threads join main
# -------------------------------------------------#

import time
import requests
import threading
# import utilities

# log = utilities.configure_logger('default', 'newsapi.log')

WORD = "trump"
NEWS_API_KEY = "29a5f72c3ba04484921a19d5aad8af48"
base_url = 'https://newsapi.org/v1/'

titles = []

def split_list(a_list):
    half = int(len(a_list)/2)
    return a_list[:half], a_list[half:]

def worker(lock, param):
    global titles
    print("hello from thread %s" % threading.current_thread().name)
    for news in param:
        lock.acquire()
        titles = get_articles(news)
        lock.release()


def get_sources():
    """"
    Get all the english language sources of news

    :param:

    :returns: list of sources

    'https://newsapi.org/v1/sources?language=en'
    """

    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources

def get_articles(source):
    """"
    Gets the articles from the sources

    :param: list of news sources

    :returns: list of titles
    """

    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              # "sortBy": "latest", # some sources don't support latest
              "sortBy": "top",
              # "sortBy": "popular",
              }
    print("requesting:" + source + ", thread %s" % threading.current_thread().name)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:  # aiohttpp has "status"
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    # the url to the article itself is in data['articles'][i]['url']
    news_titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return news_titles

def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count

def main():

    global titles
    start = time.time()
    sources = get_sources()
    sources1, sources2 = split_list(sources)
    # split two lists down to about 15 items each
    # newsapi limits the number of requests per 24 hours
    sources3, sources4 = split_list(sources2)

    lock = threading.Lock()

    # create threads and fill title list
    t1 = threading.Thread(target=worker, args=(lock, sources3,), name='t1')
    t2 = threading.Thread(target=worker, args=(lock, sources4,), name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # create reports from title list
    art_count = 0
    word_count = 0
    art_count += len(titles)
    word_count += count_word('trump', titles)
    print("===Given this number of sources: " + str(len(sources3) + len(sources4)) + "===")
    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))

if __name__ == '__main__':
    main()

