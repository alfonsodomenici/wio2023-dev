from flask import Flask

#flask application factory function
def create_app():
    app = Flask(__name__)
    return app