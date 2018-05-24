#!/usr/bin/env python3

# -------------------------------------------------#
# Title: simple.py
# Dev: Scott Luse
# Date: 05/06/2018
# -------------------------------------------------#

'''
simple.py with logging
1. All messages logged to the console
2. Warning and higher sent to date.log
3. Errors sent to syslogserver.py
'''

import logging
import logging.handlers
from datetime import date

#two formats, one with date, one without date
format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatsys = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

#today's date for log file name
logtoday = str(date.today())
logtoday = logtoday.replace("-", "") + ".log"

#two formatters, one with date, one without date
formatter = logging.Formatter(format)
formattersys = logging.Formatter(formatsys)

file_handler = logging.FileHandler(logtoday)
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

# Handler for syslog server on Windows
sys_handler = logging.handlers.DatagramHandler('127.0.0.1', 514)
sys_handler.setLevel(logging.ERROR)
sys_handler.setFormatter(formattersys)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(console_handler)               
logger.addHandler(sys_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)