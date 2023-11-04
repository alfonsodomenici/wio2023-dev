class Config:
    SECRET_KEY = 'my secret..'
    TESTING=False
    
    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING=True

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

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