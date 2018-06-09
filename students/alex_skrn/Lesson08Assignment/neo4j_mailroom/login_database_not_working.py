"""This module was expected to login to my neo4j cloud db.

This module is similar to a module in the activity repo. but it does not
behave as I expected. I wanted to use it as follows:
In other modules, namely, add_data.py and mailroom.py, I wanted to write:

import login_database
driver = login_database.login_neo4j_cloud()

However, this results in the the following error:
ServiceUnavailable: Cannot acquire connection to Address(host='hobby-opmhmhgpkde
hgbkejbochpal.dbs.graphenedb.com', port=24786)

This is way I had to move this code directly to both add_data.py
and mailroom.py.
"""

import configparser
from pathlib import Path
from neo4j.v1 import GraphDatabase, basic_auth

config_file = Path(__file__).parent.parent / 'neo4j_mailroom/.config/config'
# config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
# import ipdb; ipdb.set_trace()


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

if __name__ == "__main__":
    login_neo4j_cloud()
