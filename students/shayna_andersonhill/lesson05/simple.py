import logging
import datetime
from logging import handlers

format_time = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
#formatted ="%(filename)s:%(lineno)-4d %(levelname)s %(message)s"

filename_format = datetime.datetime.today().strftime('%Y-%m-%d') + ".log"

formatter_time = logging.Formatter(format_time)
#formatter = logging.Formatter(formatted)

file_handler = logging.FileHandler(filename_format)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter_time)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter_time)

server_handler = logging.handlers.SysLogHandler(address=('0.0.0.0', 12123))
server_handler.setLevel(logging.ERROR)
#server_handler.setFormatter(formatter)

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
