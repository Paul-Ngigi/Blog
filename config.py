class Config:
    """
    General configuration class
    """
    pass


class ProdConfig(Config):
    """
    Production configuration class
    """
    pass

class DevConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True
    

config_option = {
    'production': ProdConfig,
    'development': DevConfig
}