import time
import requests
import threading

WORD = "America"
NEWS_API_KEY = "edbcf19c9bc14326ab698f3713c80574"
base_url = 'https://newsapi.org/v1/'
titles = []


def get_sources():
    """
    Gets all sources
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
    Gets all articles
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top",
              }
    print("requesting:" + source + ", thread %s" % threading.current_thread().name)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return titles


def count_word(word, titles):
    """
    Counts specified word in titles
    """
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


def split_list(a_list, wanted_parts=1):
    """
    Splits the list of sources into a variable amount of parts
    """
    length = len(a_list)
    return [a_list[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts)]


def acquire_release(lock, sub_source_list):
    """
    Initiates the threads
    """
    global titles
    print("initiating thread %s" % threading.current_thread().name)
    for item in sub_source_list:
        lock.acquire()
        titles = get_articles(item)
        lock.release()


def run_program():
    """
    Performs the source data manipulation and threading operations
    """
    # start the timer
    start = time.time()
    # get the sources
    sources = get_sources()
    # split the list of sources
    source_list = (split_list(sources, wanted_parts=4))
    sl_1 = source_list[0]
    sl_2 = source_list[1]
    sl_3 = source_list[2]
    sl_4 = source_list[3]
    # designate the lock
    lock = threading.Lock()
    # create the threads
    thread_1 = threading.Thread(target=acquire_release, args=(lock, sl_1,), name='thread 1')
    thread_2 = threading.Thread(target=acquire_release, args=(lock, sl_2,), name='thread 2')
    thread_3 = threading.Thread(target=acquire_release, args=(lock, sl_3,), name='thread 3')
    thread_4 = threading.Thread(target=acquire_release, args=(lock, sl_4,), name='thread 4')
    # start the threads
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    # join the threads
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    # create report
    art_count = 0
    word_count = 0
    for source in sources:
        titles = get_articles(source)
        art_count += len(titles)
        word_count += count_word(WORD, titles)

    print("The number of sources:  " + str(len(sl_1) + len(sl_2) + len(sl_3) + len(sl_4)))
    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))


if __name__ == '__main__':
    run_program()

# Results::
# The number of sources: 60
# America found 19 times in 566 articles
# Process took 59 seconds

# I thought it would have ran faster!
# There is a lot to learn on this subject, and it's really cool
