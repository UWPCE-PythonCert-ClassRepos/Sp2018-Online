import logging

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
# logging.basicConfig(level=logging.WARNING, format=format, filename='mylog.log')


 # Create a "formatter" using our format string
formatter = logging.Formatter(format)
# Create a log message handler that sends output to the file 'mylog.log'
file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter we created a
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Get the "root" logger. More on that below.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def my_fun(n):
    for i in range(0,n):
        if i == 50:
            logging.warning("The vaule of i is 50")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero var i was {}".format(i))

if __name__ == '__main__':
    my_fun(100)