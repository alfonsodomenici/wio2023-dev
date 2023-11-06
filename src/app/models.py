from datetime import datetime
from src.app import db

class Wio(db.Model):
    __tablename__ = 'wio'
    id = db.Column(db.Integer, primary_key=True)
    wio = db.Column(db.String(45), nullable=False, default='wio terminal')
    macaddress = db.Column(db.String(45), unique=True)
    code = db.Column(db.String(45), nullable=False)

    @staticmethod
    def from_json(json):
        pass 

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