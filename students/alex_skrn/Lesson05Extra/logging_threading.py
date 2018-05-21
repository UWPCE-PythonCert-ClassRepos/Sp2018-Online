#!/usr/bin/env python3

"""Logging from multiple threads.

To simplify things a bit I removed syslog logging and I still
have one function only, so that not to confuse me even more.

Am I moving in the right direction with what I have now?

Issue 1: At this point I have troubles wrapping logging-related code into
a function and running it repeatedly in the main block because
in such case loggers multiply quickly and produce many repeated
log records. This is why I keep all log definions global.

Issue 2. Another unclear thing is that part about "Make sure the threads exit
after its done with execution". Why would
I need them after execution? I thought the purpose of threads was just
to run some code within them. So that thread.start() launches a thread
together with some function/program associated
with it (i.e. threading(target=my_fun)), and as soon as the associated
program is over, I don't need this thread any longer, isn't it?

Issue 3. I don't understand what grep is. From what I see in the Internet,
it is about using regular expressions for pattern matching, is that right?
Do I need to use regexps at all to search for uuid? It seems that no two
persons on the Internet can agree on the right regexp for uuid. Why
can't I just put uuid identifier at the log beginning and then use it as a key
like I do below?

I am really sorry for so much text.


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

#  DEFINING ALL LOGGERS HERE

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
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)

# Get the "root" logger.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ONE FUNCTION WHOSE EXECUTUION IS LAUNCHED BY THREADS
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
    # RUNNING 4 THREADS. join() thing is still too complicated for me to grasp
    # threads = []
    for i in range(1, 5):
        thread = threading.Thread(target=my_fun,
                                  name=str(uuid.uuid4()),
                                  args=(100,))
        # threads.append(thread)
        thread.start()

    # for thread in threads:
    #     thread.join()

    # Read from the log file using uuid as a key and print results
    my_log_file = "{}.log".format(todays_date)
    result = {}
    with open(my_log_file, 'r') as f:
        for line in f:
            key = str(line[:36])
            value = str(line[36:])
            try:
                result[key].append(value)
            except KeyError:

                result[key] = [value]

    print("\nSTARTING TO PRINT\n")
    for key, value in result.items():
        print(key)
        for v in value:
            print(v)
