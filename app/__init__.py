import logging

import falcon

from app.config import DevConfig, ProdConfig, configs
from app.middleware import Crossdomain, JSONTranslator
from app.resources.root import RootResources, RootNameResources
from app.util.logs import setup_logging
from app.util.connection import connect

def create_app(env, **kwargs):
    log_level = kwargs.get('log_level', None)
    create_log(env, log_level)

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
    log_level = kwargs.get('log_level', None)
    create_log(env, log_level)

    return connect()


def create_log(env, log_level):
    if env == 'DEV':
        configs = DevConfig
    elif env == 'PROD':
        configs = ProdConfig
    else:
        configs = DevConfig

    if log_level:
        log_level = configs.LOG_LEVEL

    setup_logging(log_level)


def create_route(app):
    app.add_route('/', RootResources())
    app.add_route('/{name}', RootNameResources())
