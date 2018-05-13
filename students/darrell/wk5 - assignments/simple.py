#simple.py
import logging, logging.handlers, datetime

'''
Level	Numeric value
CRITICAL	50
ERROR	    40
WARNING	    30
INFO	    20
DEBUG	    10
NOTSET	     0
'''

# handler creation
def create_handler(type,log_level,format_options):
    if type == 'file':
        h = logging.FileHandler(f'{datetime.datetime.now().strftime("%Y-%m-%d")}.log')
    elif type == 'console':
        h = logging.StreamHandler()
    elif type == 'syslog':
        h = logging.handlers.SysLogHandler(address=('127.0.0.1',1542))
    else:
        raise ValueError('Invalid Handler Type')

    h.setLevel(log_level)
    h.setFormatter(logging.Formatter(' '.join(format_options)))

    return h


# add root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# add file handler
logger.addHandler(create_handler('file','WARNING',['%(asctime)s',
                                                    '%(filename)s',
                                                    '%(lineno)-3d',
                                                    '%(levelname)s',
                                                    '%(message)s',
                                                    ]))

# add console handler
logger.addHandler(create_handler('console','DEBUG',['%(asctime)s',
                                                    '%(filename)s',
                                                    '%(lineno)-3d',
                                                    '%(levelname)s',
                                                    '%(message)s',
                                                    ]))
# add syslog handler
logger.addHandler(create_handler('syslog','ERROR',['%(filename)s',
                                                    '%(lineno)-3d',
                                                    '%(levelname)s',
                                                    '%(message)s',
                                                    ]))

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 5:
            logging.warning("The value of i is 5.")
        try:
            i / (5 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(10)