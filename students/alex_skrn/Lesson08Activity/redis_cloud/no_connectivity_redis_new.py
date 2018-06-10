"""This code attempts to establish connection with my redis cloud db.

I can't establish connection.
"""
""""
This info is contained in my redis db account. Don't know if it matters
dbname = "mailroom"
endpoint = "redis-18488.c16.us-east-1-2.ec2.cloud.redislabs.com:18488"
user = "alex

PS. After a sample config file was added to the lesson repo, I understood
the meaning of the above info, i.e. host and port parameters.

Now my redis db connection is fine, but I am not sure that in the remaining
week I'll have time to complete the redis-related part of the assignment.
"""

import configparser
from pathlib import Path
import redis

# GETTING USER AND PASSWORD DATA FROM CONFIG FILE
config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
config.read(config_file)
pw = config["configuration"]["pw"]
# host = 'localhost' # Is this the correct way to do it? Don't I have to set it up somehow?
host = "redis-18488.c16.us-east-1-2.ec2.cloud.redislabs.com"
# port = 6379 # Is this the correct way to do it? Don't I have to set it up somehow
port = 18488
r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)
r.set('foo', 'bar')
"""
ON WINDOWS:
redis.exceptions.ConnectionError: Error 10061 connecting to localhost:6379.
No connection could be made because the target machine actively refused it.

ON MAC: redis.exceptions.ConnectionError: Error 61 connecting to localhost:6379.
Connection refused.
"""
result = r.get('foo')
print(result)

# NEVER GOT TO THAT:
print(r.get('foo'))
