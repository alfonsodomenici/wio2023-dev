class Config:
    SECRET_KEY = 'my secret..'
    TESTING=False
    JSON_SORT_KEYS=False
    
class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class DevelopmentConfig(Config):
    DEBUG=True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///wio.db" 
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://wio2023:wio2023@localhost:3306/wio2023"
class ProductionConfig(Config):
    DEBUG=False

config = {
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'production' : ProductionConfig,

    'default': DevelopmentConfig
}