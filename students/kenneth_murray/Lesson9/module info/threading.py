import sys
import threading
import time

def func():
    for i in xrange(5):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(1)

threads = []
for i in xrange(3):
    thread = threading.Thread(target=func, args=())
    thread.start()
    threads.append(thread)



"""sub classing Threads"""
 import threading

class MyThread(threading.Thread):

    def run(self):
        print("hello from %s" % threading.current_thread().name)

thread = MyThread()
thread.start()

