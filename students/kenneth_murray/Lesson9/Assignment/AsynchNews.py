import aiohttp  # developed for async ClientSession
import asyncio
import time
import requests

WORD = "trump"

NEWS_API_KEY = "3660a22fe4704ee3bc3226fc6ac63421"

base_url = 'https://newsapi.org/v1/'

# doesn’t really need to to async since this call is only made once to gather all news sources


async def get_sources(sources):
    """Get news sources"""
    url = base_url + "sources"
    params = {"language": "en"}
    session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            data = await resp.json()
            print('Got the sources')
    sources.extend([src['id'].strip() for src in data['sources']])



async def get_articles(source):
    "../vl/articles?source=associated-press&sortBy=top&apiKey=…"
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top"
              }
    print("requesting", source)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            if resp.status_code != 200:
                print(f'something went wrong. {source}')
                await asyncio.sleep(0)  # releases control the the mainloop
                return
            data = await resp.json()  # awaits reponse rather than waiting on responese in the requests version of this
    titles.extend([(str(art['title']) + str(art['description'])) for art in data['ariticles']])


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


start = time.time()

loop = asyncio.get_event_loop()

sources = []
titles = []

# get the sources this is essentially synchronous
loop.run_until_complete(get_sources(sources))

# run the loop for the articles
jobs = asyncio.gather(*(get_articles(source) for source in sources))
loop.run_until_complete(jobs)
loop.close()

art_count = len(titles)
word_count = count_word(WORD, titles)

print(f'found {word}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')
