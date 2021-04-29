from flask import Flask
from config import config_option
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    
    # Initializing the application
    app = Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_option[config_name])
    
    # Initializing our extensions
    bootstrap.init_app(app)
    
    return app