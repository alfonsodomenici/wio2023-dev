from datetime import datetime
from src.app import db
from .exceptions import ValidationError
class Wio(db.Model):
    __tablename__ = 'wio'
    id = db.Column(db.Integer, primary_key=True)
    wio = db.Column(db.String(45), nullable=False, default='wio terminal')
    macaddress = db.Column(db.String(45),
        nullable=False, 
        unique=True)
    code = db.Column(db.String(45), nullable=False)

    @staticmethod
    def from_json(json):
        if json.get('wio') is None:
            raise ValidationError('wio is empty')
        if json.get('macaddress') is None:
            raise ValidationError('macaddress is empty')
        if json.get('code') is None:
            raise ValidationError('code is empty')
        return Wio(wio=json.get('wio'),
            macaddress=json.get('macaddress'),
            code=json.get('code'))

    def to_json(self):
        return {
            'id':self.id,
            'wio':self.wio,
            'macaddress':self.macaddress,
            'code': self.code
        }

    def to_json_slice(self):
        return {
            'wio':self.wio
        }
class WioData(db.Model):
    __tablename__ = 'wiodata'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(45), nullable=False)
    id_wio = db.Column(db.Integer, db.ForeignKey('wio.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now()) 

    def to_json(self):
        return {
            'value':self.value,
            'type': self.type,
            'wio_id': self.id_wio
        }