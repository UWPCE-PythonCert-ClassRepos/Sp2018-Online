"""
    module that will login to the various demonstration databases consistently
"""

import configparser
from pathlib import Path
import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth


config_file = Path(__file__).parent.parent / '.config/config.ini'
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    print('Here is where we use the connect to mongodb.')
    print('Note use of f string to embed the user & password (from the tuple).')
    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}''@cluster0-shard-00-00-3hjim.mongodb.net:27017,''cluster0-shard-00-01-3hjim.mongodb.net:27017,''cluster-shard-00-02-3hjim.mongodb.net:27017/test''?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
   # client = pymongo.MongoClient(f'mongodb://{user}:{pw}'
    #                             '@cluster0-shard-00-00-wphqo.mongodb.net:27017,'
     #                            'cluster0-shard-00-01-wphqo.mongodb.net:27017,'
        #                         'cluster0-shard-00-02-wphqo.mongodb.net:27017/test'
         #                        '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

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

    log.info('Here is where we use the connect to redis.')

    try:
        print(f"host {host}, port: {port}, password: {pw}")
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        print(f'error: {e}')

    return r


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    print('Here is where we use the connect to neo4j.')
    print('')

    config.read(config_file)

    graphenedb_user = config["neo4j_cloud"]["user"]
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    graphenedb_url = 'bolt://hobby-oklmfkohpmongbkebkgbdgbl.dbs.graphenedb.com:24786'

    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver
