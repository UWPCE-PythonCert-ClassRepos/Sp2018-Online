# loggingtest.py

import logging

logging.critical("This is a critical error!")
logging.error("I'm an error.")
logging.warning("Hello! I'm a warning.")
logging.info("This is some information.")
logging.debug("Perhaps this information will help you find your problem?")

# Default level without using logging.basicConfig, or some other means is:
#  WARNING. So, info and debug are not shown.
