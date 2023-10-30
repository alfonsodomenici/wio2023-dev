from flask import Blueprint

main = Blueprint('main',__name__)

#@app.route('/welcome', methods=['GET'])
@main.get('/welcome')
def welcome():
    return 'welcome'

@main.route('/login')
def login():
    return 'login'