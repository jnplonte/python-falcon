class BaseConfig(object):
    APP_NAME = 'falcon boilerplate'
    ENV = ''
    LOG_LEVEL = ''
    DB_CONNECTION = 'mysql' # support mysql for now
    DB_HOST = ''
    DB_PORT = ''
    DB_DATABASE = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''


class DevConfig(BaseConfig):
    ENV = 'DEV'
    LOG_LEVEL = 'DEBUG'
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_DATABASE = 'falcon_test'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'johnpaul'


class ProdConfig(BaseConfig):
    ENV = 'PROD'
    LOG_LEVEL = 'INFO'


configs = DevConfig
