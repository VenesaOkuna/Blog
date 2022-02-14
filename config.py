import os


class Config:
    '''
    General configuration parent class
    '''
    
    RANDOM_QUOTE_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'you-will-never-guess-this'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venesa:1234@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venesa:1234@localhost/blog'


class DevConfig(Config):
    '''
    Development  configuration child class

    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venesa:1234@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}