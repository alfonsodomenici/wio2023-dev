import os
from flask import Flask,jsonify, make_response
from http import HTTPStatus
from src.app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    pass