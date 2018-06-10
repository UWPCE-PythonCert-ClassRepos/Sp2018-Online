"""
    module that will login to the various demonstration databases consistently
"""

import configparser
from pathlib import Path
import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth


config_file = Path(__file__).parent / '.config/config.ini'
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]
        uri = config["mongodb_cloud"]["uri"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}' + uri)

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

    try:
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        print(f'error: {e}')

    return r


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    config.read(config_file)

    graphenedb_user = config["neo4j_cloud"]["user"]
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    #graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
    graphenedb_url = config["neo4j_cloud"]["url"]
    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver
