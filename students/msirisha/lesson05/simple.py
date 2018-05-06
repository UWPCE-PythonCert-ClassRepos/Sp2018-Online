#!/Users/sirisham/.virtualenvs/course2/bin/python
#simple.py
import logging
import logging.handlers
from datetime import datetime
format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

log_file = '{:%Y-%m-%d}.log'.format(datetime.now())
formatter = logging.Formatter(format)

# want to log messages level WARNING or higher to file
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

# Want to log all log messages to the console
console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.NOTSET)          
console_handler.setFormatter(formatter)          

format_without_date  = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter_without_date = logging.Formatter(format_without_date)

# want to log messages ERROR level or higher to syslog
syslog_handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 1074))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter_without_date)

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
