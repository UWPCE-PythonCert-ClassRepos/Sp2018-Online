import threading
from queue import Queue
import time

start = time.time()

def fun(n):
    n += 5
    m = n*10
    return n, m

results = Queue()

def qfun(*args):
    results.put(fun(*args))

threads = []
for i in range(0, 10):
    thread = threading.Thread(target=qfun, args=(i,))
    threads.append(thread)
    print(f'starting thread {i}')
    thread.start()

tot1 = 0
tot2 = 0
for thread in threads:
    res = results.get()
    tot1 += res[0]
    tot2 += res[1]
    print(f'joining thread {thread}')
    thread.join()

print(f'tot1 = {tot1}, tot2 = {tot2}, done in {time.time() - start}')

