#!/usr/bin/env python3

"""Logging and debugging lesson."""

import logging


format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
# Create a "formatter" using our format string
formatter = logging.Formatter(format)

# Setting up a formatter for the syslog logger - no time stamp
format2 = "%(filename)s:%(lineno)-4d %(levelname)s %(message)s"
syslog_formatter = logging.Formatter(format2)

# Create a log message handler that sends output to the file 'mylog.log'
file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter)

# default stream: sys.stderr stream one of two system streams that
# get printed directly to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Setting up a syslog server logger for Windows
syslog_handler = logging.DatagramHandler("127.0.0.1", 514)
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(syslog_formatter)

# Setting up a syslog server logger for Mac
syslog_handler = logging.SysLogHandler()
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(syslog_formatter)

# Get the "root" logger.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
logger.addHandler(file_handler)
logger.addHandler(console_handler)


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
