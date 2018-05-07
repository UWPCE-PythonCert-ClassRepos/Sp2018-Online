#simple.py
import logging
import syslogserver

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_sys = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter_sys = logging.Formatter(format_sys)

file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

sys_log_handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 1074))
sys_log_handler.setLevel(logging.INFO)
sys_log_handler.setFormatter(formatter_sys)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(sys_log_handler)

small_server = syslogserver()

def my_fun(n):
    for i in range(0, n):
        logging.info(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)