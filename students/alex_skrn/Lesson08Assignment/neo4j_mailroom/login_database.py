"""This module will login to my neo4j cloud db"""

import configparser
from pathlib import Path
from neo4j.v1 import GraphDatabase, basic_auth

config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()


def login_neo4j_cloud():
    """Connect to neo4j and login."""
    config.read(config_file)
    graphenedb_user = config["configuration"]["user"]
    graphenedb_pass = config["configuration"]["pw"]
    graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user,
                                                  graphenedb_pass
                                                  )
                                  )

    return driver
