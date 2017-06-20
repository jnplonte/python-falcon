import logging

import falcon

from app.config import DevConfig, TestConfig, ProdConfig, configs
from app.middleware import Crossdomain, JSONTranslator
from app.resources.root import RootResources, RootNameResources
from app.util.logs import setup_logging
from app.util.connection import connect

def create_app(env, **kwargs):
    create_log(env, **kwargs)

    logger = logging.getLogger(configs.APP_NAME)
    logger.info('Starting {} in {} mode'.format(configs.APP_NAME, configs.ENV))

    app = falcon.API(
        middleware=[
            Crossdomain(),
            JSONTranslator()
        ]
    )

    create_route(app)

    return app


def create_table(env, **kwargs):
    create_log(env, **kwargs)

    return connect()


def create_log(env, **kwargs):
    if env == 'DEV':
        configs = DevConfig
    elif env == 'TEST':
        configs = TestConfig
    elif env == 'PROD':
        configs = ProdConfig
    else:
        configs = DevConfig

    log_level = kwargs.get('log_level', configs.LOG_LEVEL)
    if log_level:
        setup_logging(configs.LOG_LEVEL)


def create_route(app):
    app.add_route('/', RootResources())
    app.add_route('/{name}', RootNameResources())
