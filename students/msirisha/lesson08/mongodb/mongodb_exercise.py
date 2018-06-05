"""
This program establishes the connection to mongo db. And reads/writes data from mongo db using pymongo.
"""
import configparser
import pymongo
import log

logger = log.get_logger("nosql_mongo.log", "./")

sofa_records = [
            {
                'product_type': 'sofa',
                'color': 'red',
                'in_stock_quantity': 20
            },
            {
                'product_type': 'sofa',
                'color': 'green',
                'in_stock_quantity': 5
            }]

couch_records = [
        {
            'product': 'red couch',
            'in_stock_quantity': 10
        },
        {
            'product': 'blue couch',
            'in_stock_quantity': 3
        }]


def login_mongodb_cloud():
    """
    Connect to mongdodb and login
    :return: client
    """
    try:
        # read config file
        config_parser = configparser.ConfigParser()
        config_parser.read('../.config/config')

        user = config_parser["mongodb_cloud"]['user']
        pw = config_parser["mongodb_cloud"]['pw']
        logger.info("Establishing connection to mongodb using mongo client")
        client = pymongo.MongoClient(f'mongodb://{user}:{pw}''@cluster0-shard-00-00-3hjim.mongodb.net:27017,''cluster0-shard-00-01-3hjim.mongodb.net:27017,''cluster-shard-00-02-3hjim.mongodb.net:27017/test''?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

    except Exception as e:
        logger.error("Caught exception as {} while establishing connection to mongodb".format(e))
        return None

    return client


def store_records_to_mongodb():
    """
    This method establishes connection to mongodb and writes to mongodb and queries the records.
    :return:
    """
    logger.info('Setup the connection to mongodb')
    with login_mongodb_cloud() as client:
        logger.info("We are going to use data base called dev")
        db = client['dev']

        # collections a.k.a tables in RDBMS
        logger.info("Step 1: In dev database create a collection called furniture")
        furniture = db['furniture']

        logger.info("Step 2: Inserting couch records {} in furniture collection\n".format(couch_records))
        furniture.insert_many(couch_records)

        logger.info("Step 3: inserting sofa records {} in furniture collection\n".format(sofa_records))
        furniture.insert_many(sofa_records)

        logger.info("Step 4: separating product fields into two items as product type and product color\n")
        # products with red couch matching query
        query = {'product': 'red couch'}
        logger.info('Find the products with matching query {}'.format(query))
        results = furniture.find_one(query)
        logger.info("Amending the records that updated as product to type and color")
        furniture.update_one({'_id': results['_id']}, {"$set": {'product_type': 'couch', 'color': 'red'}})
        furniture.update_one({'_id': results['_id']}, {"$unset": {'product': results['product']}})

        # products with blue couch matching query
        query = {'product': 'blue couch'}
        logger.info('Find the products with matching query {}'.format(query))
        results = furniture.find_one(query)
        logger.info("Amending the records that updated as product to type and color")
        furniture.update_one({'_id': results['_id']}, {"$set": {'product_type': 'couch', 'color': 'blue'}})
        furniture.update_one({'_id': results['_id']}, {"$unset": {'product': results['product']}})

        query = {'product_type': 'sofa'}
        logger.info('step 5: Find the products with matching query {}'.format(query))
        results = furniture.find(query)
        for item in results:
            logger.info(item)

        query = {'product_type': 'couch'}
        logger.info('Step 6: Find the products with matching query {}'.format(query))
        results = furniture.find(query)
        for item in results:
            logger.info(item)

        query = {'color': 'red'}
        logger.info('Step 7: Find the products with matching query {}'.format(query))
        results = furniture.find(query)
        for item in results:
            logger.info(item)
    db.drop_collection(furniture)


if __name__ == "__main__":
    store_records_to_mongodb()






