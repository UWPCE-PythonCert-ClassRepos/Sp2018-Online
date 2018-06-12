#!/usr/bin/env python

"""
Regular synchronous script to see how much a given word is mentioned in the
news today

Took about 21 seconds for me.

Uses data from the NewsAPI:

https://newsapi.org

NOTE: you need to register with the web site to get a KEY.
"""
import time
import requests
import threading
import queue 

WORD = "trump"

NEWS_API_KEY = "84d0483394c44f288965d7b366e54a74"

base_url = 'https://newsapi.org/v1/'


def get_sources():
    """
    Get all the english language sources of news

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
    """
    https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=1fabc23bb9bc485ca59b3966cbd6ea26
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              # "sortBy": "latest", # some sources don't support latest
              "sortBy": "top",
              # "sortBy": "popular",
              }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:  # aiohttpp has "status"
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    # the url to the article itself is in data['articles'][i]['url']
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

# start the timer
start = time.time()

# create queue for threading 
results = queue.Queue()

# fetch all sources 
sources = get_sources()

# function that puts all the functions together
# given a list of sources, this function initializes 
# the article count and word count at zero, and then
# gets articles from each source and counts the 
# occurences of the word 'trump'. This replaces the
# integrate function from the integration example. 
def search_atricles(source_chunk):
    art_count = 0
    word_count = 0
    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word('trump', titles)
    return (word_count, art_count)

# the worker function puts the results into the queue
def worker(*args):
    results.put(search_atricles(*args))


# set number of threads 
thread_count = 50
chunk_size = int(len(sources)/thread_count)
for i in range(thread_count):
    start_index = i * chunk_size
    end_index = start_index + chunk_size
    thread = threading.Thread(target  = worker, args = (sources[start_index:end_index],))
    thread.start()
    print("Thread %s started" % thread.name)

total_articles = 0
total_word_occurrences = 0
for i in range(thread_count):
    thread_result = results.get()
    total_word_occurrences = thread_result[0]
    total_articles = thread_result[1]


print(WORD, "found {} times in {} articles".format(total_word_occurrences, total_articles))
print("Process took {:.0f} seconds".format(time.time() - start))
