#simple.py
"""
You want ALL log messages logged to the console.
The format of these messages should include the current time.
You want WARNING and higher messages logged to a file named {todays-date }.log.
The format of these messages should include the current time.
You want ERROR and higher messages logged to a syslog server.
The syslog server will be appending its own time stamps to the messages that it receives,
so DO NOT include the current time in the format of the log messages that you send to the server.
"""
import logging
import datetime

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
sys_error_format = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
sys_error_formater = logging.Formatter(sys_error_format)
warn_log_name = str(datetime.date.today())

file_handler = logging.FileHandler(warn_log_name + '_Warning.log')
file_error_handler = logging.FileHandler(warn_log_name + 'sys_error.log')

file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

file_error_handler.setLevel(logging.ERROR)
file_error_handler.setFormatter(sys_error_formater)

console_handler = logging.StreamHandler()
console_handler.setLevel(0)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(file_error_handler)
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
