import time
import requests
import threading
import queue 

WORD = "trump"

NEWS_API_KEY = "bb48c72ecfad4363afdf6fc9131b50b1"

base_url = 'https://newsapi.org/v1/'


def get_sources():

    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


def get_articles(source):

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

start_time = time.time() 
results = queue.Queue() 
sources = get_sources()

def search(temp):
    art_count = 0
    word_count = 0
    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word('trump', titles)
    return (word_count, art_count)

def worker(*args):
    results.put(search(*args))

thread_count = 50
temp = int(len(sources)/thread_count)
for i in range(thread_count):
    start_index = i * temp
    end_index = start_index + temp
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
print("Process took {:.0f} seconds".format(time.time() - start_time))