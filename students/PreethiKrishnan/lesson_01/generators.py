#Method to find sum of 2 integers
def intsum(len_num):
    n = 0
    final_list = []
    if (len_num == 0 or len_num == 1):
        yield n
        #print(n)
    else:
        for i in range(len_num):
            #print("This is the list number {}".format(i))
            n += i
            yield n
            #final_list.append(n)
    #print(n)
    #print("This is the sum list: {}".format(final_list))

#Method for doubler
def doubler(len_num):
    previous_value = 1
    final_list = []
    for i in range(1, len_num):
        if(i == 1):
            final_list.append(i)
            next_value = i
        else:
            next_value = previous_value*2
            final_list.append(next_value)
            previous_value = next_value
    yield next_value
    #print(next_value)
    print("This is doubler list: {}".format(final_list))

#Method for fibonacci
def fib(len_num):
    series = [1,1]
    for i in range(len_num):
        new_num = series[i] + series[i+1]
        series.append(new_num)
    yield series
    print("This is the fibonacci list: {}".format(series))

#Method for Prime numbers
def prime(len_num):
    #print("entering prime")
    prime_list = []
    for i in range(2, len_num):
        count = 2
        new_count = 0
        while(count <= i):
            if(i%count == 0):
                new_count += 1
            count += 1
        if(new_count == 1):
            prime_list.append(i)
    yield prime_list
    print("This is the list of prime numbers: {}".format(prime_list))

if __name__ == '__main__':
    print(intsum(3))
    print(intsum(0))
    print(doubler(2))
    print(fib(10))
    print(prime(10))