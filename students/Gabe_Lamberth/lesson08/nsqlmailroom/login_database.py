#!/usr/bin/env python3
"""
    I'm not interested in redis. I don't like
"""

import configparser
from pathlib import Path
import pymongo
from neo4j.v1 import GraphDatabase, basic_auth

import utilities

log = utilities.configure_logger('default', '../logs/login_databases_dev.log')
config_file = Path(__file__).parent.parent / '.config/config.ini'
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    log.info('Here is where we use the connect to mongodb.')
    log.info('Note use of f string to embed the user & password (from the tuple).')
    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}@cluster0-shard-00-00-l5eez.mongodb.net:27017,'
                                 'cluster0-shard-00-01-l5eez.mongodb.net:27017,'
                                 'cluster0-shard-00-02-l5eez.mongodb.net:27017/test'
                                 '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')

    return client


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    log.info('Here is where we use the connect to neo4j.')
    log.info('')

    config.read(config_file)

    graphenedb_user = config["neo4j_cloud"]["user"]
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    graphenedb_url = config["neo4j_cloud"]["url"]
    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver
