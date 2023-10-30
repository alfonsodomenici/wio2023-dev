from flask import Flask,jsonify, make_response
from http import HTTPStatus
from src.app import create_app

app = create_app('default')