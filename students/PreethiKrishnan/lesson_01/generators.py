import itertools

#Method to find sum of 2 integers
def intsum():
    sum = 0
    num = 0
    while True:
        yield sum
        num += 1
        sum += num

#Method to find sum of 2 integers
def intsum2():
    sum = 0
    num = 0
    while True:
        yield sum
        num += 1
        sum += num


#Method for doubler
def doubler():
    previous_value = 1
    current_value = 1
    while True:
        yield current_value
        previous_value += 1
        current_value = previous_value*2

#Method for fibonacci
def fib():
    first_num, second_num = 1, 1
    while True:
        yield first_num
        new_num = first_num + second_num
        first_num = second_num
        second_num = new_num

#Method for Prime numbers
def prime_numbers():
    prime_list = []
    len_num = itertools.count(start=2, step=1)
    for i in len_num:
        count = 2
        new_count = 0
        while(count <= i):
            if(i%count == 0):
                new_count += 1
            count += 1
        if(new_count == 1):
            prime_list.append(i)
            yield i


