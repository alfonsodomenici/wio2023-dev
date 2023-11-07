import os
from flask import Flask,jsonify, make_response
from http import HTTPStatus
from src.app import create_app
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    pass


from src.app.models import Wio, WioData

