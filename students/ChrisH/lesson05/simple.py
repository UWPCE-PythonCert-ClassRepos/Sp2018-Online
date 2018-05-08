# simple.py

import logging
import logging.handlers

import datetime


format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_syslog = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter_syslog = logging.Formatter(format_syslog)

syslog_handler = logging.handlers.DatagramHandler('localhost', 514)
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter_syslog)

file_handler = logging.FileHandler(datetime.datetime.now().isoformat()[:10] + '.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(syslog_handler)
logger.setLevel(logging.DEBUG)
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
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))


if __name__ == "__main__":
    my_fun(100)



