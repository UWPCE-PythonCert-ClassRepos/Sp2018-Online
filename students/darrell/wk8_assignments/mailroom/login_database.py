"""
    module that will login to the various demonstration databases consistently
"""
import os
import configparser
# from pathlib import Path
import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth
import utilities

log = utilities.configure_logger('default', 'logs/mailroom.log')
config_file = os.path.abspath('../nosql/config/config.ini')
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """
    user = ''
    pw = ''
    config_string = ''
    log.info('Here is where we use the connect to mongodb.')
    log.info('Note use of f string to embed the user & password (from the tuple).')
    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]
        config_string = config["mongodb_cloud"]["connection"]
        log.info(f'config_string ::::: {config_string}')

    except Exception as e:
        raise(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}{config_string}')

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
        raise(f'error: {e}')

    log.info('Here is where we use the connect to redis.')

    try:
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        raise(f'error: {e}')

    return r


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    log.info('Here is where we use the connect to neo4j.')
    log.info('')

    config.read(config_file)

    graphenedb_user = config["neo4j_cloud"]["user"]
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    graphenedb_url = config["neo4j_cloud"]["connection"]
    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver
