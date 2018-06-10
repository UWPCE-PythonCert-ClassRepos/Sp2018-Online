#!/usr/bin/env python

""" Threading script to see how much a given word is mentioned in the
news today.

With 1 thread:
trump found 52 times in 564 articles
Process took 37 seconds

With 2 threads:
trump found 52 times in 564 articles
Process took 19 seconds

With 3 threads:
trump found 52 times in 565 articles
Process took 14 seconds

4 threads:
trump found 52 times in 565 articles
Process took 10 seconds

Then I ran into <Response [429]>
{"status":"error","code":"rateLimited","message":"You have made too many request
s recently. Developer accounts are limited to 1,000 requests over a 24 hour peri
od (250 requests available every 6 hours). Please upgrade to a paid plan if you
need more requests."}

PS. After 6 hours I tried again.

10 threads
trump found 63 times in 567 articles
Process took 5 seconds

15 threads:
trump found 63 times in 567 articles
Process took 4 seconds

20 threads:
trump found 63 times in 567 articles
Process took 3 seconds

30 threads:
trump found 63 times in 567 articles
Process took 3 seconds

Then I ran into Response 429 again. At this point I checked how much
time it takes to run the async version, and the result was as follows:
trump found 62 times in 567 articles
Process took 2 seconds


Uses data from the NewsAPI:

https://newsapi.org

NOTE: you need to register with the web site to get a KEY.
"""
import time
import requests
import threading
import queue

WORD = "trump"

NEWS_API_KEY = "149a8dc71fff41bdbb24a186ac089667"

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
    """Return number of occurrences of word in titles."""
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


def main_func(sources):
    """Return number of occurrences of "trump" and number of articles."""
    art_count = 0
    word_count = 0
    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word('trump', titles)

    return (word_count, art_count)


start = time.time()  # Measure time

sources = get_sources()  # Sources of data

results = queue.Queue()  # Use a queue to put results of main_func execution


def putting_on_queue(*args):
    """Put things on queue to retrieve later."""
    results.put(main_func(*args))


# Break work (i.e. sources) into chunks and put each into a thread
num_threads = 40  # Number of threads to use
dx = int(len(sources) / num_threads)  # Width of the chunk of sources
for i in range(num_threads):
    x0 = int(dx * i)  # Get indices to index into the source of data
    if num_threads != 1 and i == num_threads - 1 and len(sources) % 2 != 0:
        x1 = int(x0 + dx + 1)  # If num of elements is odd, last chunk + 1 item
    else:
        x1 = int(x0 + dx)
    thread = threading.Thread(target=putting_on_queue,
                              args=(sources[x0:x1],)
                              )
    thread.start()

# Putting together results from the queue
word_count = 0
art_count = 0
for i in range(num_threads):
    result = results.get()
    word_count += result[0]
    art_count += result[1]
print(WORD, "found {} times in {} articles".format(word_count, art_count))


print("Process took {:.0f} seconds".format(time.time() - start))
