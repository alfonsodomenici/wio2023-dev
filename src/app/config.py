class Config:
    SECRET_KEY = 'my secret..'
    TESTING=False

class TestingConfig(Config):
    TESTING=True

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///wio.db" 
class ProductionConfig(Config):
    DEBUG=False

config = {
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'production' : ProductionConfig,

    'default': DevelopmentConfig
}