#!/usr/bin/env python
"""
Using threading to grab news items from newsapi.org

Ref: https://www.youtube.com/watch?v=NwH0HvMI4EA

End result of running the program:
trump found 82 times in 562 articles
process took 25 seconds

"""

import threading
from queue import Queue
import time
import requests

WORD = "trump"

NEWS_API_KEY = "60265484a72c4bda85f93c95a44b4d63"

base_url = 'https://newsapi.org/v1/'

news_lock = threading.Lock()


# What job are we going to have these workers do
def news_job(worker):
    """
    This function defines the job we are going to have these workers perform.
    """
    time.sleep(0.5)  # half a second

    with news_lock:
        print(threading.current_thread().name, worker)


def threader():
    """
    Function to perform the actual threading operation.
    """
    while True:
        worker = q.get()
        news_job(worker)
        q.task_done()


# Taken from the class videos
def get_sources():
    """Get news sources"""
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("here are all of the sources")
    print(sources)
    return sources


def get_articles(source):
    """get the articles from the sources"""
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top",
              }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Something Very Bad Has Happened with {)".format(source))
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


def main():
    """
    Function as main entry point for running the program.
    """
    start = time.time()
    sources = get_sources()

    art_count = 0
    word_count = 0

    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word(WORD, titles)

    # Number of threads we will work with
    for x in range(2):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    # We want to do 20 jobs
    for worker in range(20):
        q.put(worker)

    q.join()

    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("process took {:.0f} seconds".format(time.time() - start))


if __name__ == '__main__':
    q = Queue()
    main()
