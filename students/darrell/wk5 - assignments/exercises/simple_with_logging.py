import logging


logging.basicConfig(level=logging.WARNING)
def my_fun(n):
    logging.warning(f'Function my_fun called with value {n}')
    for i in range(0,n):
        logging.debug(i)
        i / (50 - i)

if __name__ == '__main__':
    my_fun(100)