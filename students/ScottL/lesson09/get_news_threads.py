#!/usr/bin/env python

# -------------------------------------------------#
# Title: get_news_threads.py
# Dev: Scott Luse
# Date: 06/11/2018
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
#
# Update 6/11/2018: code is updated but newsAPI request
# limitation is blocking full testing. However, the
# output.txt file shows the results using 4 threads
# doesn't help the speed
# -------------------------------------------------#

import time
import requests
import threading

WORD = "trump"
NEWS_API_KEY = "29a5f72c3ba04484921a19d5aad8af48"
base_url = 'https://newsapi.org/v1/'

titles = []


def split_list_many(alist, wanted_parts):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

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
    list_sources = split_list_many(sources, wanted_parts=4)

    lock = threading.Lock()

    threads = []
    for i in range(4):
        thread = threading.Thread(target=worker, args=(lock, list_sources[i],))
        thread.start()
        threads.append(threads)
        thread.join()

    '''
    <Response [429]> is blocking development and code is not tested
    {"status":"error","code":"rateLimited","message":"You have made too many
    requests recently. Developer accounts are limited to 1,000 requests over
    a 24 hour period (250 requests available every 6 hours). Please upgrade
    to a paid plan if you need more requests."}
    '''

    # create reports from title list
    art_count = 0
    word_count = 0
    art_count += len(titles)
    word_count += count_word('trump', titles)
    print("===Given this number of sources: " + str(len(sources)) + "===")
    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))

if __name__ == '__main__':
    main()

