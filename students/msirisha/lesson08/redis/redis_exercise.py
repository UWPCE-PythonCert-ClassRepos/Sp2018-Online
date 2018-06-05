import configparser
import log

logger = log.get_logger("nosql_redis.log", "./")


def login_redis_cloud():
    """
        connect to redis and login
    """
    try:
        # read config file
        config_parser = configparser.ConfigParser()
        config_parser.read('../.config/config')

        host = config_parser["redis_cloud"]['host']
        pw = config_parser["redis_cloud"]['pw']
        port = config_parser["redis_cloud"]['port']

    except Exception as e:
        logger.error(f'error: {e}')

    logger.info('Here is where we use the connect to redis.')

    try:
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        logger.error(f'error: {e}')

    return r

