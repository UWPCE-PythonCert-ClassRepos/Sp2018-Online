# -*- coding: utf-8 -*-
"""
Created on Sun May  6 08:37:32 2018

@author: seelc
"""

#simple.py
import logging
import time
import logging.handlers

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)

#Server formatter includes just the levelname and messages, no date
#This will be used with the server handler
server_format = "%(levelname)s %(message)s"
server_formatter = logging.Formatter(server_format)

#Changed file handler to name file with the date
file_handler = logging.FileHandler(time.strftime("%d-%m-%Y") + '.log')
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

#Creating console handler, setting to DEBUG level, and adding formatter
console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

#Adding a third handler for the server
#using the server_formatter without the date
server_handler = logging.handlers.DatagramHandler("127.0.0.1", 514)
server_handler.setLevel(logging.ERROR)
server_handler.setFormatter(server_formatter)

#Adding all three handlers to the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(console_handler)  
logger.addHandler(server_handler)             

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
            
        #Need to log to the server, file, and console
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))


if __name__ == "__main__":
    my_fun(100)