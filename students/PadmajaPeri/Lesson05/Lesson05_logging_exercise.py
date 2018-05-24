import logging
import time
from logging.handlers import SysLogHandler

# Constant that represents the port that the server listens on. This server
# will get the logs
SYSLOG_UDP_PORT = 514

# Formatter for logs written to stream and file
format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter = logging.Formatter(format)

# Logs written to syslog server do not include the timestamp. Create a new
# formatter for it
syslog_format = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
syslog_formatter = logging.Formatter(syslog_format)

# Log handler that writes to a file.
file_name = time.strftime("%d-%m-%Y") + ".log"
file_handler = logging.FileHandler(file_name)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

# Log handler that writes to a stream.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Log handler that writes to a server.
syslog_handler = SysLogHandler(address=('localhost', SYSLOG_UDP_PORT))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(syslog_formatter)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(syslog_handler)


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
