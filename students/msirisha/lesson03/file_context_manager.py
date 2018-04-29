#!/usr/bin/env python3
from contextlib import contextmanager
# file context manager


class File(object):
    def __init__(self, file, mode):
        print("In init")
        self.file = file
        self.mode = mode
        self.mode = mode

    def __enter__(self):
        print("In __enter__")
        self.file_handle = open(self.file, self.mode)
        return self.file_handle

    def __exit__(self, *args):
        print("In exit {}".format(*args))
        self.file_handle.close()


# File context manager using contextmanager decorator
files = []
for _ in range(1):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)


@contextmanager
def open_file(file, mode):
    the_file = open(file, mode)
    yield the_file
    the_file.close()


files = []
for x in range(1):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
