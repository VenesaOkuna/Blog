from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)


    # Creating the app configurations
    app.config.from_object(config_options['development'])


    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)


    #will add views and forms

    return app