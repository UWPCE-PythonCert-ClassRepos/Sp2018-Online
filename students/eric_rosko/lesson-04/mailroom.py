#!/usr/bin/env python3

'''
Eric Rosko
Session03
mailroom.py
Tuesday, Nov. 16, 2015
Description:
    Part Session 3 homework
Requirements:
    You must have py.test installed from http://pytest.org
    python3 -m pip install pytest
Usage:
    py.test -v mailroom.py
    or
    python3 mailroom.py
'''

import json_save_meta as js
from operator import *
import io

class DictionarySaver(js.JsonSaveable):
    dict = js.Dict()
    def __init__(self, dict):
        self.dict = dict

def send_thank_you(data):
    isNameEntered = False
    while not isNameEntered:
        fullname = input("Enter full name: ")
        if fullname == "list":
            print(get_donor_names(data))
        else:
            isNameEntered=True

    if not is_person_in_database(data,fullname):
        print("User not in database - adding.")
        data[fullname]=[]

    isNumber = False
    while not isNumber:
        amount = input("Enter donation amount: ")
        if verify_number(float(amount)):
            isNumber=True

    add_donation_for_person(data,fullname,float(amount))
    print_thank_you_email(fullname, amount)

def print_thank_you_email(name, amount):
    print("Thank you {} for your generous donation of ${}!".format(name,amount))

def print_report(data):

    output=""
    sortedKeys=[]
    results = {}

    for i in data:
        aList=data[i]
        for j in aList:
            total = sum(aList)
            count = len(aList)
            avg = float(total / count)

            results[i] = {'total':total, 'count':count,'average':avg}

    myNewList = sorted(results.items(), key=lambda x: getitem(x[1],'total'))
    myNewList.reverse()

    for item in myNewList:
        output += "Donor:{}\tTotal:{:.2f}\tCount:{}\t\tAverage:{:.2f}\n".format(item[0], item[1]['total'], item[1]['count'],item[1]['average'])
    return output

def verify_number(input):
    if not isinstance(input, (int,float)):
        return False
    return True

def is_person_in_database(database, person):
    if person not in database:
        return False
    return True

def add_donation_for_person(database, person, amount):
    try:
        donations = database[person]
    except KeyError:
        database[person]=[]
        donations = database[person]

    donations.append(amount)

def get_donor_names(data):
    output=''
    # the sort is just to make testing easier
    for name in sorted(data.keys()):
        if len(output) > 0:
            output += ', '
        output+=name

    return output

def save_to_file(data):
    ds = DictionarySaver(data)
    saved = ds.to_json_compat()

    with open('temp.json', 'w') as tempfile:
        tempfile.write(str(saved))

def load_from_file():
    with open("temp.json") as tempfile:
        ds2 = DictionarySaver(tempfile.read())

    print(type(data)) # <class 'str'>
    # assert type(data) == type(dict), "data no longer a dict!"

    # somehow this turns out data into a string
    return ds2.dict

    # print('contents\n', contents, '\n')
    # ds2 = DictSaver(contents)

    # print(type(ds2._dictionary)) # <class 'str'>

    # xx = js.Dict.to_python(contents)


if __name__ == "__main__":
    isRunning=True
    data = dict(one=[1.01], two=[2.01,2.02], three=[3.01,3.02,3.03], four=[.5])
    while isRunning:
        choice = input("1.) Send thank you\n"
                       "2.) Create a report\n"
                       "3.) Save to file\n"
                       "4.) Load from file\n"
                       "Choice (q to quit):" )

        if choice == 'q':
            isRunning=False
        elif choice == '1':
            send_thank_you(data)
        elif choice == '2':
            print(print_report(data))
        elif choice == '3':
            save_to_file(data)
        elif choice == '4':
            data = load_from_file()
        else:
            print ("Bad input: {}\n".format(choice))
