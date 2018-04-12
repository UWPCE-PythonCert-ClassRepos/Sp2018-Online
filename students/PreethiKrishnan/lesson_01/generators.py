#Method to find sum of 2 integers
def sum_of_integers(len_num):
    n = 0
    final_list = []
    for i in range(len_num):
        #print("This is the list number {}".format(i))
        n += i
        final_list.append(n)
    print("This is the sum list: {}".format(final_list))

#Method for doubler
def doubler(len_num):
    previous_value = 1
    final_list = []
    for i in range(1, len_num):
        if(i == 1):
            final_list.append(i)
            #print("This is the list number {}".format(i))
            #print("This is doubler: {}".format(i))
        else:
            next_value = previous_value*2
            #print("This is doubler: {}".format(next_value))
            final_list.append(next_value)
            previous_value = next_value
    print("This is doubler list: {}".format(final_list))

#Method for fibonacci
def fibonacci_series(len_num):
    series = [1,1]
    for i in range(len_num):
        new_num = series[i] + series[i+1]
        series.append(new_num)
    print("This is the fibonacci list: {}".format(series))

#Method for Prime numbers
def prime_numbers(len_num):
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
            #print(prime_list)
    print("This is the list of prime numbers: {}".format(prime_list))


sum_of_integers(10)
doubler(10)
fibonacci_series(10)
prime_numbers(10)