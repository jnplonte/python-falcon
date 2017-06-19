class BaseConfig(object):
    APP_NAME = 'falcon boilerplate'
    ENV = ''
    LOG_LEVEL = ''


class DevConfig(BaseConfig):
    ENV = 'DEV'
    LOG_LEVEL = 'DEBUG'


class TestConfig(BaseConfig):
    ENV = 'TEST'
    LOG_LEVEL = 'NOTSET'


class ProdConfig(BaseConfig):
    ENV = 'PROD'
    LOG_LEVEL = 'INFO'


configs = DevConfig
