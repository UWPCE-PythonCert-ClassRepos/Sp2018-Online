import requests
import threading
import queue
import time

WORD = "Trump"
NEWS_API_KEY = 'd622dd804f1c44a78a0c8bcab6f387c9'
base_url = 'https://newsapi.org/v1/'


def get_sources():
    """https://newsapi.org/v1/sources?language=en"""
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print('all the sources')
    print(sources)
    return sources


def get_articles(source):
    """../vl/articles?source=associated-press&sortBy=top&apiKey=…"""
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


def count_word(word, title):
    word = word.lower()
    count = 0
    if word in title.lower():
        count += 1
    return count


def run_thread(input_queue, i, output_queue):
    while True:
        source = input_queue.get()
        print(f"Thread {i}: Getting titles for {source}...")
        titles = get_articles(source)
        for title in titles:
            output_queue.put(title)
        input_queue.task_done()


start = time.time()
sources = get_sources()

art_count = 0
word_count = 0
worker_thread = queue.Queue()
output_thread = queue.Queue()
num_threads = 2
results = []

for i in range(num_threads):
    worker = threading.Thread(target=run_thread, args=(worker_thread, i, output_thread))
    worker.setDaemon(True)
    worker.start()

for source in sources:
    worker_thread.put(source)

worker_thread.join()
while output_thread.empty() is not True:
    results.append(output_thread.get())

for element in results:
    # print(element)
    art_count += 1
    word_count += count_word(WORD, element)

print(f'found {WORD}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')