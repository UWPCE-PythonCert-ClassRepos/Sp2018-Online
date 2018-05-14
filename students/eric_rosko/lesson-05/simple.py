#!/usr/bin/env python3
# simple.py

'''
Assignment: Lesson 5
Author: Eric Rosko
Date: 5/8/2018
'''

import logging
import logging.handlers
from time import localtime, strftime, asctime

from syslogserver import *

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
format_no_time = "%(lineno)-4d %(levelname)s %(message)s"


formatter = logging.Formatter(format)
formatter_no_time = logging.Formatter(format_no_time)

file_handler = logging.FileHandler(strftime("%Y-%m-%d.log", localtime()))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

remote_handler = logging.handlers.SysLogHandler(address=('0.0.0.0', 514))
remote_handler.setLevel(logging.ERROR)
remote_handler.setFormatter(formatter_no_time)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(remote_handler)


def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:                                   # Add this line
            logging.warning("The value of i is 50.")  # Add this line

        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)

    # logging.critical("This is a critical error!")
    # logging.error("I'm an error.")
    # logging.warning("Hello! I'm a warning!")
    # logging.info("This is some information.")
    # logging.debug("Perhaps this information will help you find your problem?")
