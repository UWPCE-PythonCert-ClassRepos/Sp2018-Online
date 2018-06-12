import threading

import requests
import time
import config
import queue

SEARCH_WORD = "trump"
NEWS_API_KEY = config.api_key

base_url = "https://newsapi.org/v1/"

def get_sources():
    """
    Get all the english language sources of news

    https://newsapi.org/v1/sources?language=en
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
    Get all the articles from sources
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
    """count occurences of word in titles, returns the count"""
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count

def threads(sources, results):
    def worker(*args):
        results.put(get_articles(*args))

    for source in sources:
        thread = threading.Thread(target=worker, args=(source,))
        thread.start()
        print("Thread %s started" % thread.name)

    return results

if __name__ == "__main__":
    results = queue.Queue()
    start = time.time()

    sources = get_sources()

    word_count = 0
    art_count = 0
    results = threads(sources, results)

    while not results.empty():
        article_list = results.get()
        art_count += len(article_list)
        word_count += count_word(SEARCH_WORD, article_list)

    print(SEARCH_WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))