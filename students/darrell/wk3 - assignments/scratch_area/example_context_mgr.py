from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print('hello')


class Tag():

    def __init__(self, tag_name, content):
        self.tag_name = tag_name
        self.content = content

    def __enter__(self):
        self.result = '<{}>{}</{}>'.format(self.tag_name,self.content,self.tag_name)
        return self.result

    def __exit__(self,*args):
        print(*args)

with Tag('h1','hello') as myTag:
    print(myTag)