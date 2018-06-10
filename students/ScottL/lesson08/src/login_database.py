#!/usr/bin/env python3

# -------------------------------------------------#
# Title: mailroom menu
# Dev: Scott Luse
# Date: 06/02/2018
# Change log:
# -------------------------------------------------#

import configparser
from pathlib import Path
import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth

import utilities

log = utilities.configure_logger('default', '../logs/login_databases_dev.log')
config_file = Path(__file__).parent.parent / '.config/config.ini'
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    log.info('Connect to mongodb.')
    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}'
                                 '@cluster0-shard-00-00-yl9gv.mongodb.net:27017,'
                                 'cluster0-shard-00-01-yl9gv.mongodb.net:27017,'
                                 'cluster0-shard-00-02-yl9gv.mongodb.net:27017/test'
                                 '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')

    return client


def login_redis_cloud():
    """
        connect to redis and login
    """
    try:
        config.read(config_file)
        host = config["redis_cloud"]["host"]
        port = config["redis_cloud"]["port"]
        pw = config["redis_cloud"]["pw"]


    except Exception as e:
        print(f'error: {e}')

    log.info('Connect to redis.')

    try:
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        print(f'error: {e}')

    return r


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    log.info('Connect to neo4j.')
    log.info('')

    config.read(config_file)

    graphenedb_user = config["neo4j_cloud"]["user"]
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    graphenedb_url = 'bolt://hobby-kencbepahikogbkedmgmfgbl.dbs.graphenedb.com:24786'
    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver
