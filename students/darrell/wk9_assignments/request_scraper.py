import requests
import time
from concurrent import futures
NEWS_API_KEY = '989fec61f847423189c7d1f4e92871fc'

base_url = 'https://newsapi.org/v1/'
WORD = "war"


def get_sources():
    "https://newsapi.org/v1/sources?language=en"
    url = base_url + "sources"
    params = {"language": "en", "apiKey": NEWS_API_KEY}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print('List of Sources:', sources)
    return sources


def get_articles(source):
    "../vl/articles?source=associated-press&sortBy=top&apiKey=…"
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


start = time.time()
sources = get_sources()

art_count = 0
word_count = 0
# with futures.ProcessPoolExecutor() as pool:
#     for source in sources:
#         titles = get_articles(source)
#         art_count += len(titles)
#         word_count += count_word(WORD, titles)
with futures.ProcessPoolExecutor() as pool:
    for titles in pool.map(get_articles, sources):
        art_count += len(titles)
        word_count += count_word(WORD, titles)

print(f'found {WORD}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')
