#!/usr/bin/env python
"""
Starting point for lesson9 assignment - Ken Murray
"""

import time
import requests
import threading

WORD = "trump"

NEWS_API_KEY = "3660a22fe4704ee3bc3226fc6ac63421"

base_url = 'https://newsapi.org/vl/'

titles = []


def split_list(a_list):
    half = int(len(a_list) / 2)
    return a_list[:half], a_list[half:]


def threader(lock, param):
    global titles
    print("hello from thread %s" % threading.current_thread().name)
    for news in param:
        lock.acquire()
        titles = get_articles(news)
        lock.release()


def get_sources():
    "https://newsapi.org/vl/sources?language=en"
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


def get_articles(source):
    "../vl/articles?source=associated-press&sortBy=top&apiKey=�"
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top",
              }
    print("requesting:" + source + ", thread %s" % threading.current_thread().name)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return titles


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


#    start = time.time()
sources = get_sources()
sources1, sources2 = split_list(sources)
sources3, sources4 = split_list(sources2)

lock = threading.Lock()

# create threads and fill title list
t1 = threading.Thread(target=threader, args=(lock, sources3,), name='t1')
t2 = threading.Thread(target=threader, args=(lock, sources4,), name='t2')

t1.start()
t2.start()

t1.join()
t2.join()

# create reports from title list
art_count = len(titles)
word_count = count_word(WORD, titles)

print(f'found {"trump"}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')
