from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

jwt = JWTManager()

#flask application factory function
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.json.sort_keys = False
    
    db.init_app(app)

    jwt.init_app(app)
    
    from src.app.main.views import main
    app.register_blueprint(main,url_prefix='/')

    from src.app.api.rest_api import api
    app.register_blueprint(api, url_prefix='/api')

    return app