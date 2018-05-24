#!/usr/bin/env python3

"""Logging and debugging lesson."""

import logging
import datetime
from logging import handlers


format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
# Create a "formatter" using our format string
formatter = logging.Formatter(format)

# Setting up a formatter for the syslog logger - no time stamp
format2 = "%(filename)s:%(lineno)-4d %(levelname)s %(message)s"
syslog_formatter = logging.Formatter(format2)

# Create a log message handler that sends output to the file 'todays_date.log'
todays_date = str(datetime.date.today())
file_handler = logging.FileHandler("{}.log".format(todays_date))
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter)

# default stream: sys.stderr stream one of two system streams that
# get printed directly to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# UNCOMMENT IF ON WINDOWS
# Setting up a syslog server logger for Windows
# syslog_handler_w = handlers.DatagramHandler("127.0.0.1", 514)
# syslog_handler_w.setLevel(logging.ERROR)
# syslog_handler_w.setFormatter(syslog_formatter)

# COMMENT OUT THE FOLLOING 3 LINES IF ON WINDOWS
# # Setting up a syslog server logger for Mac
syslog_handler_m = handlers.SysLogHandler()
syslog_handler_m.setLevel(logging.ERROR)
syslog_handler_m.setFormatter(syslog_formatter)

# Get the "root" logger.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# UNCOMMENT THE FOLLOWING LINE IF ON WINDOWS
# logger.addHandler(syslog_handler_w)
# COMMENT OUT THE FOLLOING LINE IF ON WINDOWS
logger.addHandler(syslog_handler_m)


def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            msg = "Tried to divide by zero. Var i was {}. Recovered gracefully"
            logging.error(msg.format(i))


if __name__ == "__main__":
    my_fun(100)
