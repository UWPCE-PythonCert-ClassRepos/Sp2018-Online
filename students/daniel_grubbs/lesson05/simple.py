#!/usr/bin/env python3
"""


Filename: simple.py
References:

"""
import logging
import logging.handlers
import logging.config
from datetime import datetime

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
# Define the format of that will be presented by SyslofHandler
format_remote = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

# logging.config.fileConfig('test.log')


# Formatters - specify the layout of log records in the final output
formatter = logging.Formatter(format)
# Create a "formatter" using our format string
formatter_remote = logging.Formatter(format_remote)


# Handlers - send the log records to the appropriate destination
file_handler = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

remote_handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 1514))
remote_handler.setLevel(logging.ERROR)
remote_handler.setFormatter(formatter_remote)

# Loggers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(remote_handler)


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
