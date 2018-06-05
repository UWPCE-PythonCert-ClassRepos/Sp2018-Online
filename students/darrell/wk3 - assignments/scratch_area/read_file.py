

with open('test.txt','r') as file:
    data = file.readlines()
    data1 = file.read()
    print(type(data))
    print(type(data1))
