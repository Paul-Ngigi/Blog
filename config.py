import os


class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:pass@localhost/blog'


class ProdConfig(Config):
    """
    Production configuration class
    """

class DevConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True
    

config_option = {
    'production': ProdConfig,
    'development': DevConfig
}