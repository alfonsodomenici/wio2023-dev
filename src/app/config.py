import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my secret..'
    TESTING=False
    JSON_SORT_KEYS=False   
    
    @staticmethod
    def init_app(app):
        pass


    
class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or "sqlite://"

class DevelopmentConfig(Config):
    DEBUG=True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or "sqlite:///wio.db" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "mysql+mysqlconnector://wio2023:wio2023@localhost:3306/wio2023"
class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or \
        "mysql+mysqlconnector://wio2023:wio2023@localhost:3306/wio2023"
class DockerConfig(ProductionConfig):

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

config = {
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'production' : ProductionConfig,
    'docker' : DockerConfig,
    'default': DevelopmentConfig
}