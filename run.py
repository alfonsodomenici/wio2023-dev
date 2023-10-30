from flask import Flask,jsonify, make_response
from http import HTTPStatus
from src.app import create_app

app = create_app()

#@app.route('/welcome', methods=['GET'])
@app.get('/')
def welcome():
    return {'message':'ciao da wio2023'},HTTPStatus.CREATED 