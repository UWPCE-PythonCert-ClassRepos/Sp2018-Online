import logging


def get_logger(file, path):
    formatter= "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    log_file = path + "/" + file
    formatter = logging.Formatter(formatter)

    # want to log messages level WARNING or higher to file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Want to log all log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.NOTSET)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
