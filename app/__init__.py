from flask import Flask
from config import config_option
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy


def create_app(config_name):
    
    # Initializing the application
    app = Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_option[config_name])
    
    # Initializing our extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    # Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app