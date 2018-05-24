import logging
import syslogserver
from logging import handlers
from datetime import datetime, timezone

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"

# Create a "formatter" using our format string
formatter = logging.Formatter(format)
format_wo_date  = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_wo_date = logging.Formatter(format_wo_date)

# Setting up a formatter for the syslog logger - no time stamp
format_syslog = "%(filename)s:%(lineno)-4d %(levelname)s %(message)s"
syslog_formatter = logging.Formatter(format_syslog)

# Log message handler to send output to the file 'today's date.log'
log_name = datetime.now(timezone.utc).strftime("%Y%m%d") + '.log'
file_handler = logging.FileHandler(log_name)
file_handler.setLevel(logging.WARNING)

# Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter)

# default stream: sys.stderr stream one of two system streams that
# get printed directly to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Log ERROR level messages and higher to syslog
syslog_handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 514))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(format_wo_date)
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
            msg = "Tried to divide by zero. Var i was {}. Recovered gracefully"
            logging.error(msg.format(i))


if __name__ == "__main__":
    my_fun(100)