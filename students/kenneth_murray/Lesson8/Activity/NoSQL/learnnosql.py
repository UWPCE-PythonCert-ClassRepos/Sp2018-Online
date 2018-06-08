#!/usr/bin/env python3
"""

Integrated example for nosql databases
Lesson 8
Ken Murray


"""

import learn_data
import mongodb_script
import redis_script
import neo4j_script
import simpler_script
import utilities


def showoff_databases():
    """
    Here we illustrate basic interaction with nosql databases
    """

    log = utilities.configure_logger('default', '..//logs//nosql_dev.log')

    log.info("Mongodb example to use data from Furniture module, so get it")
    furniture = learn_data.get_furniture_data()

    mongodb_script.run_example(furniture)

    log.info("Other databases use data embedded in the modules")

    redis_script.run_example()
    neo4j_script.run_example()
    simpler_script.run_example(furniture)


if __name__ == '__main__':
    """
    orchestrate nosql examples
    """
    showoff_databases()
