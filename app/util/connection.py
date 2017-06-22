import logging

from  sqlalchemy import create_engine


def connect(configs):
    if configs.DB_CONNECTION == "mysql":
        if configs.DB_PASSWORD == "":
            engine = create_engine("mysql+pymysql://%s@%s:%s/%s" % (configs.DB_USERNAME, configs.DB_HOST, configs.DB_PORT, configs.DB_DATABASE), echo=True)
        else:
            engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (configs.DB_USERNAME, configs.DB_PASSWORD, configs.DB_HOST, configs.DB_PORT, configs.DB_DATABASE), echo=True)
    else:
        engine = None
        
    logger = logging.getLogger(configs.APP_NAME)
    logger.info("connected to database")

    return engine
