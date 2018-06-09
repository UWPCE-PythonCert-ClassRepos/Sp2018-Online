import pymongo


client = pymongo.MongoClient("mongodb://user1:TNQmaU7T1vAnP9zl@cluster0-shard-00-00-yxic6.mongodb.net"
                             ":27017,cluster0-shard-00-01-yxic6.mongodb.net:27017,cluster0-shard-00-02-yxic6."
                             "mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.test

"""
mongodb://user1:TNQmaU7T1vAnP9zl@cluster0-shard-00-00-yxic6.mongodb.net:27017,cluster0-shard-00-01-yxic6.mongodb.net:27017,cluster0-shard-00-02-yxic6.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"""