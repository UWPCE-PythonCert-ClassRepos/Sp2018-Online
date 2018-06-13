import time
import requests
import threading
import queue
import logging
import configparser
from pathlib import Path


config_file = Path(__file__).parent / '.config/config.ini'
config = configparser.ConfigParser()
config.read(config_file)

WORD = "trump"

NEWS_API_KEY = config["news_api"]["api_key"]

base_url = 'https://newsapi.org/v1/'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


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
    print("Printing all the sources")
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


def invoke_worker(sources):
    """Return number of occurrences of "trump" and number of articles."""
    art_count = 0
    word_count = 0
    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word('trump', titles)

    return word_count, art_count


start = time.time()  # Measure time

sources = get_sources()  # Sources of data

results = queue.Queue()  # Use a queue to put results of worker execution


def putting_on_queue(*args):
    """Put things on queue to retrieve later."""
    results.put(invoke_worker(*args))


def main():

    # Break work (i.e. sources) into chunks and put each into a thread
    # Seem to get a response 429 when accessing the articles over 1000 times
    thread_count = 4  # Number of threads to use
    delta = int(len(sources) / thread_count)  # Width of the chunk of sources
    for i in range(thread_count):
        x0 = delta * i  # Get indices to index into the source of data
        x1 = x0 + delta
        thread = threading.Thread(target=putting_on_queue, args=(sources[x0:x1],))
        thread.start()

    # Putting together results from the queue
    word_count = 0
    art_count = 0
    for i in range(thread_count):
        result = results.get()
        word_count += result[0]
        art_count += result[1]

    print(WORD, f"found {word_count} times in {art_count} articles")
    print(f"Process took {(time.time() - start):.0f} seconds")


if __name__=="__main__":
    main()