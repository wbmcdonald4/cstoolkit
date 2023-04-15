from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8000

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    HOST = '127.0.0.1'
    PORT = 8000

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}