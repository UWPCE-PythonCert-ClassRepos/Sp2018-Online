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


def worker(sources):
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

results = queue.Queue()  # Use a queue to put results of worker execution


def putting_on_queue(*args):
    """Put things on queue to retrieve later."""
    results.put(worker(*args))


# Break work (i.e. sources) into chunks and put each into a thread
thread_count = 2  # Number of threads to use
dx = int(len(sources) / thread_count)  # Width of the chunk of sources
for i in range(thread_count):
    x0 = int(dx * i)  # Get indices to index into the source of data
    if thread_count != 1 and i == thread_count - 1 and len(sources) % 2 != 0:
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
for i in range(thread_count):
    result = results.get()
    word_count += result[0]
    art_count += result[1]

print(WORD, "found {} times in {} articles".format(word_count, art_count))
print("Process took {:.0f} seconds".format(time.time() - start))
# 1 thread
# trump found 75 times in 565 articles
# Process took 24 seconds
