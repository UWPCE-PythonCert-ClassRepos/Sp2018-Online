#!/usr/bin/env python3
"""
Follow along with the content for logging and debugging

Filename: simple_practtice.py
"""
import logging

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
# logging.basicConfig(level=logging.WARNING, format=format, filename="my_log.log")

# Create a "formatter" using our format string
formatter = logging.Formatter(format)

# Create a log message handler that sends output to the file 'mylog.log'
file_handler = logging.FileHandler("my_log.log")
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        # Let's try this gracefully
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))


if __name__ == '__main__':
    my_fun(100)
