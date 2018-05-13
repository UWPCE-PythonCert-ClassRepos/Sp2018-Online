import logging

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
logging.basicConfig(level=logging.WARNING, format=format)

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