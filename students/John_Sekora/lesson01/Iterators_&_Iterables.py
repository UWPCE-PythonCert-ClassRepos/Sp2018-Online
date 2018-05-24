# John Sekora
# Class 2, Lesson01, Iterators & Iterables
# UW Certificate in Python, 4/8/2018


class IterateMe_2(object):
    ''' This class attempts to operate with the same functionality as range() '''
    def __init__(self, start, stop, step):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration


# Let's create a class called "it"
it = IterateMe_2(2, 20, 2)

# Wonder what happens if I try and stop the iterator, can I start it again?
print("Running IterateMe_2, with numbers not greater than 10")
for i in it:
    if i > 10:
        break
    print(i)
# It stops the sequence for any numbers greater than 10

print("Rerunning IterateMe_2")
for i in it:
    print(i)

# I am shocked to see that this loop picked itself back up, but skipped the number 12
# I will see how this compares with the range() function

rn = range(2, 20, 2)

print("Running the range() function, with numbers not greater than 10")
for x in rn:
    if x > 10:
        break
    print(x)

print("Rerunning the range() function")
for x in rn:
    print(x)


# Wow, range has no special method, __next__
print(dir(range))


# These classes perform differently, and this is because both range() and IterateMe2() are iterables...
# Only Iterate_Me2() is an Iterator

