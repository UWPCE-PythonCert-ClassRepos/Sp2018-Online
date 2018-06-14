# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 08:35:54 2018

@author: seelc
"""

import threading
import time
import requests

'''Overall Structure:
    (1)get_sources
    (2)multithreaded_sources
        (3) get_articles
    (4)count_word
    
num_threads testing:
    tested num_threads with values ranging from 2-60, with 2 threads code ran 
    at roughly 30 seconds,  with 60 it took 4 seconds to run. The optimal value
    seems to be about 40 threads with a run time of 3 seconds.
    
    NOTE: count_words takes an additional 34 seconds to count the number of times trump appears,
    unsure why this takes so long but there doesnt appear to be any room for multi-threading
    since its doing all the computations internally
'''
num_threads = 40

WORD = "trump"
NEWS_API_KEY = 'b9ef465f122243db848ddc1584b03987'
sources_url = "https://newsapi.org/v1/sources?language=en&apiKey=b9ef465f122243db848ddc1584b03987"
base_url = "https://newsapi.org/v1/"

all_titles = []

def get_sources():
    
    '''uses the "sources_url" to retrieve information on sources and convert to
    a json file'''
    
    url = sources_url
    #params = {"language": "en"}
    resp = requests.get(url)
    data = resp.json()
    #print(data)
    sources = data["sources"]
    sources_list = []
    for i in sources:
        sources_list.append(i["id"])
    return sources_list



def get_articles(source, all_titles):
    
    '''Takes a source name and searches that source for any articls sorting 
    them by "top", returns "titles" holding the tile, description, and article
    information for articles from each source'''
    
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": 'b9ef465f122243db848ddc1584b03987',
              "sortBy": "top"
              }
    print("requesting", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print(f'something went wrong. {source}')
        #print(resp)
        #print(resp.text)
        return []
    data = resp.json()
    titles = [str(art['title']) + str(art['description'])
             for art in data['articles']]
    return titles
    #all_titles.append(titles)


#Making the mistake of passing the same source multiple times

def multithreaded_sources(num_threads, passed_sources, index, length, all_titles):
    
    '''Take the number of threads, a list of sources, and an index
    creates a num_threads number of threads to retrieve article information for
    each source'''
    threads = []
    for j in range(num_threads):
        #Checking to ensure we arent createing a thread for a source that doesnt exist
        if index + j < length:
            thread = threading.Thread(target = get_articles, args = (passed_sources[j],all_titles,))
            thread.start()
            print("------------------------", passed_sources[j], "----------------------")
            #print(thread.name)
            threads.append(thread)
    
    #for all_threads in threads:
        #all_threads.start()
        
    #Waiting for all threads to finish before calling join    
    for all_thread in threads:
        all_thread.join()
        

        
start = time.time()
my_sources = get_sources()
print("got sources")
titles = []


i = 0
length = len(my_sources)
while i < length:
    
    '''calls multi-threading method to append relevant article information to 
    titles'''
    
    passed_sources = my_sources[i:i + num_threads]
    titles.append(multithreaded_sources(num_threads, passed_sources, i, length, all_titles))
    i = i + num_threads
    


def count_word(word, titles):
    
    '''Pretty much exactly the same as in the video, counts occurences of the
    search word in the title'''
    
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count

    
art_count = 0
word_count = 0
for source in my_sources:
    titles = get_articles(source, all_titles)
    print(titles)
    art_count += len(titles)
    word_count += count_word(WORD, titles)

print(f'found {WORD}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')