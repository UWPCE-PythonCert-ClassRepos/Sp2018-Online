#!/usr/bin/env python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 05 - Assignment
     SUB TITLE: Logging
       CREATOR: PydPiper
  DATE CREATED: 5/6/18
 LAST MODIFIED: 5/6/18
   DESCRIPTION: Use the logger module to log different level messages at 3 different locations.
                1) Log ALL message to console, format with time-stamp
                2) Log WARNING and higher messages to a file named <todays-date>.log, format with time-stamp
                3) Log ERROR and higher messages to a local server created by syslogserver.py, with no time-stamp
********************************************************************************************************************"""

""" SAMPLE CODE - MODIFIED """
#simple.py
import logging
import datetime
from logging import handlers

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_server ="%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter_server = logging.Formatter(format_server)

filename = str(datetime.date.today()) + ".log"
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

server_handler = handlers.DatagramHandler("127.0.0.1", 514)
server_handler.setLevel(logging.ERROR)
server_handler.setFormatter(formatter_server)


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
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)
