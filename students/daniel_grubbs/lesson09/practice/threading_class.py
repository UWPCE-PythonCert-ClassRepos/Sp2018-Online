#!/usr/bin/env python3
"""
Example from class videos
"""

import random
import threading
import time

def func():
    for i in range(5):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(random.random() * 2)

func()

# threads = []
# for i in range(3):
#     thread = threading.Thread(target=func, args=())
#     thread.start()
#     threads.append(thread)
#
#
# class MyThread(threading.Thread):
#
#     def run(self):
#         print("hello from %s" % threading.current_thread().name)
#
# thread = MyThread()
# thread.start()
