"""This code attempts to establish connection with my neo4j cloud db.

This connection is successful.
"""

import configparser
from pathlib import Path
from neo4j.v1 import GraphDatabase, basic_auth

# GETTING USER AND PASSWORD DATA FROM CONFIG FILE
config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
config.read(config_file)
graphenedb_user = config["configuration"]["user"]
graphenedb_pass = config["configuration"]["pw"]
graphenedb_url = "bolt://hobby-bjkmfeabkpihgbkeddhdlgbl.dbs.graphenedb.com:24786"

# ESTABLISH CONNECTION AND EXTRACT ANY EXISTING RECORDS FROM THE DB
driver = GraphDatabase.driver(graphenedb_url,
                              auth=basic_auth(graphenedb_user, graphenedb_pass))

# with driver.session() as session:
#     session.run("MATCH (n) DETACH DELETE n")
#
with driver.session() as session:
#     for first, last in [('Bob', 'Jones'),
#                         ('Nancy', 'Cooper'),
#                         ]:
#         cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (first, last)
#         session.run(cyph)

    cyph = """MATCH (p:Person)
          RETURN p.first_name as first_name, p.last_name as last_name
       """

    result = session.run(cyph)
    for record in result:
        print(record['first_name'], record['last_name'])
