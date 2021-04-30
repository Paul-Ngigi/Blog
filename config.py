import os


class Config:
    """
    General configuration class
    """
    pass


class ProdConfig(Config):
    """
    Production configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/blog'

class DevConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True
    

config_option = {
    'production': ProdConfig,
    'development': DevConfig
}