from flask import Blueprint

api = Blueprint('api',__name__)

@api.route('')
def all():
    return [{'id':1, 'msg':'message one'},
        {'id':2, 'msg':'message two'}
    ]