import logging
import logging.handlers
import time

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_sys = "%(funcname)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter_sys = logging.Formatter(format_sys)

file_handler = logging.FileHandler('{}.log'.format(time.strftime('%m-%d-%Y_%I-%M-%S-%p')))
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter) 

syslog_handler = logging.handlers.DatagramHandler('127.0.0.1', 514)
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter_sys)         

logger = logging.getLogger()
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