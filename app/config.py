class BaseConfig(object):
    APP_NAME = 'falcon boilerplate'
    ENV = ''
    LOG_LEVEL = ''
    DB_CONNECTION = 'mysql'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_DATABASE = 'falcon_test'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'johnpaul'


class DevConfig(BaseConfig):
    ENV = 'DEV'
    LOG_LEVEL = 'DEBUG'


class ProdConfig(BaseConfig):
    ENV = 'PROD'
    LOG_LEVEL = 'INFO'


configs = DevConfig
