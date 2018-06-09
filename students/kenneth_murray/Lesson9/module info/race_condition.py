#!/usr/bin/env python3

import threading
import time


# create a mutable object that is shared among threads
class shared:
    val = 1


def func():
    y = shared.val
    time.sleep(0.00001)
    y += 1
    shared.val = y


threads = []
# with enough threads, there's sufficient overhead to
# cause a race condition
for i in range(100):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(shared.val)

"""locking"""
import threading
import time

lock = threading.Lock()

def f():
    lock.acquire()
    print("%s got lock" % threading.current_thread().name)
    time.sleep(1)
    lock.release()

threading.Thread(target=f).start()
threading.Thread(target=f).start()
threading.Thread(target=f).start()

"""nonblock lock"""
import threading
lock = threading.Lock()
lock.acquire()
if not lock.acquire(False):
    print("couldn't get lock")
lock.release()
if lock.acquire(False):
    print("got lock")

"""event loop"""
while True:
   evt = event_queue.pop()
   if evt:
       evt.call_handler()
