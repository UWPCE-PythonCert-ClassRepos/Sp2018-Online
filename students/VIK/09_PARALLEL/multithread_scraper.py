#!/usr/bin/env python3

"""********************************************************************************************************************
        TITLE: UW PYTHON 220 - Lesson 09 - Multi-threading
    SUB TITLE: Web Scraper
      CREATOR: PydPiper
 DATE CREATED: 6/9/18
LAST MODIFIED: 6/9/18
  DESCRIPTION: The GIL is release when waiting for connection. Create a newsAPI scraper that uses threading
               to search for a keyword title
********************************************************************************************************************"""

from config import NEWS_API_KEY
import requests
import time
import threading
from queue import Queue
import logging

logging.basicConfig(level=logging.DEBUG)

WORD = "war"
base_url = 'https://newsapi.org/v1/'
n_threads = 1


def get_sources():
    "https://newsapi.org/v2/sources?language=en"
    url = base_url + "sources"
    params = {"language": "en", "apiKey": NEWS_API_KEY}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print('List of Sources:', sources)
    return sources


def get_articles(source):
    "../v1/articles?source=associated-press&sortBy=top&apiKey=…"
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top"
              }
    print("requesting", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print(f'something went wrong. {source}')
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

if __name__ == "__main__":


    start = time.time()
    sources = get_sources()

    tot_sources = len(sources)
    divs = round(tot_sources / n_threads)

    # split sources into smaller bits based on thread division
    subdiv_source = [sources[i:i + divs] for i in range(0, len(sources), divs)]

    def main_run(sublist):
        art_count = 0
        word_count = 0
        for source in sublist:
            titles = get_articles(source)
            art_count += len(titles)
            word_count += count_word(WORD, titles)
        return art_count, word_count

    # store returns in queue
    results = Queue()
    def q_get_articles(*args):
        logging.info("adding {} to queue".format(args))
        results.put(main_run(*args))



    # list of threads
    threads = []
    for sublist in subdiv_source:
        thread = threading.Thread(target=q_get_articles, args=(sublist,))
        threads.append(thread)
        logging.info('starting thread')
        thread.start()

    tot_art = 0
    tot_word = 0
    for thread in threads:
        logging.info('adding {} queue resutls to collector'.format(thread))
        res = results.get()
        tot_art += res[0]
        tot_word += res[1]
        logging.info('joining thread {}'.format(thread))
        thread.join()



    print(f'found {WORD}, {tot_word} times in {tot_art} articles')
    print(f'Process took {(time.time() - start):.0f} sec.')