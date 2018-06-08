#!/usr/bin/env python3
"""

just for simplerick
Lesson 8
Ken Murray


"""

import learn_data
import simplerick_script
import utilities


def showoff_databases():
    """
    Here we illustrate basic interaction with nosql databases
    """

    log = utilities.configure_logger('default', '..//logs//nosql_dev.log')

    log.info("Other databases use data embedded in the modules")

    simplerick_script.run_example()


if __name__ == '__main__':
    """
    orchestrate nosql examples
    """
    showoff_databases()
