#simple.py
import datetime
import logging
import logging.handlers

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
syslogformat = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
syslogformatter = logging.Formatter(syslogformat)

now = datetime.datetime.now()

current_date = "%d-%d-%d" % (now.year, now.month, now.day)
file_handler = logging.FileHandler(current_date + '.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Strangely, I can only get the following to work on my system if the logging level is set to DEBUG only.
# No WARNING, No ERROR.
syslog_handler = logging.handlers.DatagramHandler("127.0.0.1", 1514)
# syslog_handler = logging.handlers.SysLogHandler(address=('localhost', 1514))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(syslogformatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
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