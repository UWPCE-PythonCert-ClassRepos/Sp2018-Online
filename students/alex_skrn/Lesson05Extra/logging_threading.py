#!/usr/bin/env python3

"""Logging from multiple threads.

I just wanted to tell that I did not ignore this problem
and I did spend considerable time researching on it,
but ultimately got stuck in all of its aspects.
Given the amount of time already spent, I think there is no point
increasing my "losses" any further because it begins to harm
my work on regular class assignments.

To simplify things a bit I removed syslog logging.

Task definition:
Add a bit more functionality to create more logging and add multiple threads.
Then Provide a uuuid in your logging that is specific to a single run of
the thread. sudo code way of explaining it:

def start_thread_to_execute_function_with_uuid_for_the_log():
    # Three logging levels done like you have above but a uuid included that
    # is common to all of them

for i in range(0, n):
   start_thread_to_execute_function_with_uuid_for_the_log()
   # Make sure the threads exits after its done with execution

You should now be able to grep your file output for a uuid and see the three
logs you created per execution.
"""

import uuid
import threading
import logging
import datetime


format = "%(threadName)s - %(filename)s: %(lineno)-4d %(levelname)s %(message)s"
# Create a "formatter" using our format string
formatter = logging.Formatter(format)

# Create a log message handler that sends output to the file 'todays_date.log'
todays_date = str(datetime.date.today())
file_handler = logging.FileHandler("{}.log".format(todays_date))
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter created above.
file_handler.setFormatter(formatter)

# default stream: sys.stderr stream one of two system streams that
# get printed directly to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Get the "root" logger.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
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
            msg = "Tried to divide by zero. Var i was {}. Recovered gracefully"
            logging.error(msg.format(i))


if __name__ == "__main__":
    threads = []
    for i in range(1, 5):
        thread = threading.Thread(target=my_fun,
                                  name=str(uuid.uuid4()),
                                  args=(100,))
        threads.append(thread)
        thread.start()

    # for thread in threads:
    #     thread.join()
