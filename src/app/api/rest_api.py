from flask import Blueprint, request
from src.app import db
from src.app.models import Wio, WioData
from http import HTTPStatus
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity

api = Blueprint('api',__name__)


@api.route('/wios/auth', methods=['POST'])
def auth():
    json = request.get_json()
    if json.get('macaddress') is None:
        return "Wio non inviato", HTTPStatus.UNAUTHORIZED

    wio = Wio.query.filter_by(macaddress=json.get('macaddress')).one_or_none()
    if wio is None:
        return "Wio non trovato", HTTPStatus.UNAUTHORIZED

    additional_claims={'macaddress':wio.macaddress}
    token = create_access_token(identity=wio.id,
        additional_claims=additional_claims)

    return {'access-token': token}

@api.route('/wios', methods=['POST'])
def registration():
    json = request.get_json()
    wio = Wio(wio=json.get('wio'),
        macaddress=json.get('macaddress'),
        code=json.get('code'))
    db.session.add(wio)
    db.session.commit()
    return wio.to_json(),201

@api.route('/wios')
def all():
    return [wio.to_json_slice() for wio in Wio.query.all()] 

@api.route('/wios', methods=['DELETE'])
@jwt_required()
def delete():
    wio = db.get_or_404(Wio,get_jwt_identity())
    db.session.delete(wio)
    db.session.commit()
    return "", 204

@api.route('/wios/data', methods=['POST'])
@jwt_required()
def add_data():
    wio = db.get_or_404(Wio,get_jwt_identity())
    json=request.get_json()
    data = WioData(value=json.get('value'),
        type=json.get('type'),
        id_wio=wio.id)
    db.session.add(data)
    db.session.commit()
    return data.to_json()

@api.route('/wios/data', methods=['GET'])
@jwt_required()
def view_data():
    wio = db.get_or_404(Wio,get_jwt_identity())
    result = WioData.query.filter_by(id_wio=wio.id).all()
    return [data.to_json() for data in result]