"""This code attempts to establish connection with my mongo cloud db.

I can't establish connection.

PS. As of 3 June 2018. A person from mongodb.com emailed me trying
to help with my connection error. I replied with more delails.
"""

import configparser
from pathlib import Path
from pymongo import MongoClient

# GETTING USER AND PASSWORD DATA FROM CONFIG FILE
config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
config.read(config_file)
user = config["configuration"]["user"]
pw = config["configuration"]["pw"]

client = MongoClient(f'mongodb://{user}:{pw}'
                        '@cluster0-shard-00-00-payac.mongodb.net:27017,'
                        'cluster0-shard-00-01-payac.mongodb.net:27017,'
                        'cluster0-shard-00-02-payac.mongodb.net:27017/test'
                        '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
                        '&retryWrites=true')

db = client['dev']
"""The value of db at this point is:
Database(MongoClient(host=['cluster0-shard-00-02-payac.mongodb.net:27017', 'clus
ter0-shard-00-00-payac.mongodb.net:27017', 'cluster0-shard-00-01-payac.mongodb.n
et:27017'], document_class=dict, tz_aware=False, connect=True, ssl=True, replica
set='Cluster0-shard-0', authsource='admin', retrywrites=True), 'dev')
"""


furniture = db['furniture']

results = furniture.insert_many([
        {
            'product': 'Red couch',
            'in_stock_quantity': 10
        },
        {
            'product': 'Blue couch',
            'in_stock_quantity': 3
        }])
"""
ON WINDOWS/MAC THE ABOVE CODE THROWS AN ERROR:
"pymongo.errors.ServerSelectionTimeoutError: No primary available for writes."
"""

# NEVER GOT TO THESE LINES:
query = {'product': 'Red couch'}
results = furniture.find_one(query)
