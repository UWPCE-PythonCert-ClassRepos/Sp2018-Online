#Sum generator

def sum_next():
    list=[0]
    while True:
        if len(list) == 1:
            yield 0
        else:
            yield sum(list)


def doubler():
    i = 1
    while True:
        if i == 1:
            yield 1
        else:
            yield i
        i *= 2

result_dbl = (x * 2 for x in range (10))

def firstn(n):
    num = 0
    while num < 0:
        yield num
        num += 1

# storelast.py
#
# An iterator that stores the last value returned.

class storelast(object):
    def __init__(self,source):
        self.source = source
    def next(self):
        item = self.source.next()
        self.last = item
        return item
    def __iter__(self):
        return self

# Example
if __name__ == '__main__':
    from follow import *
    from apachelog import *

    lines = storelast(follow(open("run/foo/access-log")))
    log   = apache_log(lines)

    for r in log:
        print r
        print lines.last

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def sum_add():
    for i in integers():
        yield i + (i+1)

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result